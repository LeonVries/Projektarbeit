

'''
### **1. Unternehmen A: `StrategyDynamic`**

Ziel: Maximierung des Gewinns durch Preisbedingte Steuerung der Produktionsauslastung durch optimale Festlegung von Frühbucher- und Last-Minute-Preisen unter Berücksichtigung von Nachfrage, Produktionskapazität und Lagerbeständen.

Funktionsweise:

1. **Preis-Kombinationen generieren:**
   - **Frühbucher-Preise (`early_price_candidates`)** und **Last-Minute-Preise (`last_price_candidates`)** werden kombiniert.
   - Für jede Kombination wird die Nachfrage (`dA_early`, `dA_lm`) basierend auf den Preisen berechnet (`market.generate_demands`).
   - Hier ist den UN die Nachfragekure & elastizität bekannt, entsprechend stark vereinfacht - in der Realtität sieht das natürlich anders aus: Hier bietet sich an mit Regressionen oä zu arbeiten im advanced Modell - Für die PA Aber irrelevant denke ich  
2. 
   - **Entscheidungsvariablen:**
     - **Binäre Variablen (`x[i]`):** Wählen ein spezifisches Preis-Szenario (1 = gewählt, 0 = nicht gewählt).
     - **Kontinuierliche Variablen:**
       - **Produktion (`prod`):** Produktionsmenge.
       - **Endlagerbestand (`inv_end`):** Lagerbestand am Periodenende.
   
   - **Einschränkungen:**
     - **Ein Szenario wählen:** Summe der `x[i]`-Variablen muss 1 sein.
     - **Produktionskapazität:** `prod` darf die maximale Kapazität nicht überschreiten.
     - **Nachfrage decken:** Für das gewählte Szenario muss die gesamte Nachfrage durch Produktion und Lagerbestand gedeckt sein.
     - **Lagerbestandspuffer:** `inv_end` muss mindestens einen festgelegten Pufferwert erreichen.

   - **Zielfunktion:**
     - **Gewinn maximieren:** Differenz zwischen Einnahmen (aus Verkäufen) und Gesamtkosten (Fixkosten, variable Produktionskosten, Lagerhaltungskosten).

3. **Modell lösen und Ergebnisse interpretieren:**
   - Der LP-Solver bestimmt die optimale Preis-Kombination und die entsprechende Produktionsmenge sowie den Endlagerbestand.
   - Rückgabe der gewählten Preise (`pe`, `pl`), Produktionsmenge (`prod`), Endlagerbestand (`inv_end`) und des erzielten Gewinns.


'''

from pulp import LpProblem, LpMaximize, LpVariable, lpSum
import numpy as np

# Unternehmen A: StrategyDynamic
class StrategyDynamic:

    def __init__(self, early_price_candidates=[60, 80, 100, 120, 140],
                 last_price_candidates=[80, 120, 160, 200],
                 demand_uncertainty=0.1):  # 10% Unsicherheit
        self.early_price_candidates = early_price_candidates
        self.last_price_candidates = last_price_candidates
        self.demand_uncertainty = demand_uncertainty

    def optimize_decision(self, company, price_B_early, price_B_last, market):
        scenarios = []
        for pe in self.early_price_candidates:
            for pl in self.last_price_candidates:
                dA_early, dA_lm, dB_early, dB_lm = market.generate_demands(pe, price_B_early, pl, price_B_last)

                # Einführung von Schätzfehlern
                uncertainty_factor_early = np.random.uniform(1 - self.demand_uncertainty, 1 + self.demand_uncertainty)
                uncertainty_factor_lm = np.random.uniform(1 - self.demand_uncertainty, 1 + self.demand_uncertainty)

                dA_early_est = dA_early * uncertainty_factor_early
                dA_lm_est = dA_lm * uncertainty_factor_lm

                scenarios.append((pe, pl, dA_early_est, dA_lm_est))

        model = LpProblem("A_decision", LpMaximize)
        x = {i: LpVariable(f"x_{i}", cat='Binary') for i, _ in enumerate(scenarios)}

        prod = LpVariable("production", lowBound=0)
        inv_end = LpVariable("inv_end", lowBound=0)

        # Sicherstellen, dass nur ein Szenario gewählt wird
        model += lpSum(x.values()) == 1

        # Produktionskapazität darf nicht überschritten werden
        model += prod <= company.capacity

        # Nachfrage decken für das gewählte Szenario
        for i, sc in enumerate(scenarios):
            pe, pl, dA_early_est, dA_lm_est = sc
            total_demand = dA_early_est + dA_lm_est
            model += total_demand * x[i] <= company.inventory + prod

        # Lagerbestands-Beschränkungen
        total_demand_expr = lpSum([x[i] * (scenarios[i][2] + scenarios[i][3]) for i in range(len(scenarios))])
        model += inv_end == company.inventory + prod - total_demand_expr
        model += inv_end >= company.buffer_stock

        # Einnahmen und Kosten
        revenue_expr = lpSum([x[i] * (scenarios[i][2] * scenarios[i][0] + scenarios[i][3] * scenarios[i][1]) for i in range(len(scenarios))])
        cost_expr = company.cost.fixed_cost + prod * (company.cost.total_unit_cost()) + inv_end * (company.cost.inventory_holding_cost)

        # Zielfunktion: Gewinn maximieren
        model += revenue_expr - cost_expr

        # Modell lösen
        model.solve()

        # Gewähltes Szenario identifizieren
        chosen = None
        for i in x:
            if x[i].varValue > 0.5:
                chosen = i
                break

        if chosen is not None:
            pe, pl, dA_early_est, dA_lm_est = scenarios[chosen]
            chosen_prod = prod.varValue
            chosen_inv = inv_end.varValue
            # Berechnung des Gewinns basierend auf den geschätzten Nachfragen
            revenue = scenarios[chosen][2] * scenarios[chosen][0] + scenarios[chosen][3] * scenarios[chosen][1]
            cost = company.cost.fixed_cost + chosen_prod * company.cost.total_unit_cost() + chosen_inv * company.cost.inventory_holding_cost
            profit = revenue - cost
            return pe, pl, chosen_prod, chosen_inv, profit, dA_early_est, dA_lm_est
        else:
            # Fallback, falls kein Szenario gewählt wird
            return company.base_price, 100, 0, company.inventory, 0, 0, 0

# Unternehmen B: StrategyStatic
class StrategyStatic:

    def __init__(self, max_adjustment=0.05):
        self.max_adjustment = max_adjustment  # maximale Anpassung (z.B. 5%)

    def adjust_price(self, own_price, competitor_price, marginal_cost):
        """
        Anpassung des Preises basierend auf der Konkurrenz:
        - Wenn eigener Preis > Konkurrenz, senke Preis leicht
        - Wenn eigener Preis < Konkurrenz, erhöhe Preis leicht
        - Begrenzung auf max_adjustment
        """
        if own_price > competitor_price:
            new_price = max(marginal_cost, own_price * (1 - self.max_adjustment))
        elif own_price < competitor_price:
            new_price = own_price * (1 + self.max_adjustment)
        else:
            # Preis gleich, kleine zufällige Anpassung
            adjustment = np.random.uniform(-self.max_adjustment, self.max_adjustment)
            new_price = max(marginal_cost, own_price * (1 + adjustment))
        return new_price
