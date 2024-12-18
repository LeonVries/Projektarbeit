from pulp import LpProblem, LpMaximize, LpVariable, lpSum
import numpy as np

# Unternehmen A: StrategyDynamic
class StrategyDynamic:
    def __init__(self, early_price_candidates=[60, 70, 80, 100, 120,130, 140],
                 last_price_candidates=[60, 70, 80, 120,140, 160, 180, 200]):
        self.early_price_candidates = early_price_candidates
        self.last_price_candidates = last_price_candidates

    def optimize_decision(self, company, price_B_early, price_B_last, market):
        # Hier wird nur noch die unternehmensinterne Unsicherheit verwendet: company.demand_uncertainty
        scenarios = []
        for pe in self.early_price_candidates:
            for pl in self.last_price_candidates:
                dA_early, dA_lm, dB_early, dB_lm = market.generate_demands(pe, price_B_early, pl, price_B_last)

                # Schätzfehler auf Basis der Unsicherheit des Unternehmens
                uncertainty_factor_early = np.random.uniform(1 - company.demand_uncertainty, 1 + company.demand_uncertainty)
                uncertainty_factor_lm = np.random.uniform(1 - company.demand_uncertainty, 1 + company.demand_uncertainty)

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
            revenue = dA_early_est * pe + dA_lm_est * pl
            cost = company.cost.fixed_cost + chosen_prod * company.cost.total_unit_cost() + chosen_inv * company.cost.inventory_holding_cost
            profit = revenue - cost
            return pe, pl, chosen_prod, chosen_inv, profit, dA_early_est, dA_lm_est
        else:
            # Fallback, falls kein Szenario gewählt wird
            return company.base_price, 100, 0, company.inventory, 0, 0, 0


# Unternehmen B: StrategyStatic
class StrategyStatic:
    def __init__(self, max_adjustment=0.15):
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
