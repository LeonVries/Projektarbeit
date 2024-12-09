from pulp import LpProblem, LpMaximize, LpVariable, lpSum
import numpy as np

class StrategyDynamic:
    """
    Komplexe Optimierungsstrategie für Stufe 3:
    Wählt aus verschiedenen Preis-Kombinationen (Frühbucher/Last-Minute) das beste Szenario.
    """
    def __init__(self, early_price_candidates=[60, 80, 100, 120, 140],
                 last_price_candidates=[80, 120, 160, 200]):
        self.early_price_candidates = early_price_candidates
        self.last_price_candidates = last_price_candidates

    def optimize_decision(self, company, price_B_early, price_B_last, market):
        scenarios = []
        for pe in self.early_price_candidates:
            for pl in self.last_price_candidates:
                dA_early, dA_lm, dB_early, dB_lm = market.generate_demands(pe, price_B_early, pl, price_B_last)
                scenarios.append((pe, pl, dA_early, dA_lm))

        model = LpProblem("A_decision", LpMaximize)
        x = {i: LpVariable(f"x_{i}", cat='Binary') for i, _ in enumerate(scenarios)}

        prod = LpVariable("production", lowBound=0)
        inv_end = LpVariable("inv_end", lowBound=0)

        # Ensure only one scenario is chosen
        model += lpSum(x.values()) == 1

        # Production cannot exceed capacity
        model += prod <= company.capacity

        # For each scenario, ensure demand can be met
        for i, sc in enumerate(scenarios):
            pe, pl, dA_early, dA_lm = sc
            total_demand = dA_early + dA_lm
            model += total_demand * x[i] <= company.inventory + prod

        # Inventory constraints
        total_demand_expr = lpSum([x[i] * (scenarios[i][2] + scenarios[i][3]) for i in range(len(scenarios))])
        model += inv_end == company.inventory + prod - total_demand_expr
        model += inv_end >= company.buffer_stock

        # Revenue and Cost expressions
        revenue_expr = lpSum([x[i] * (scenarios[i][2] * scenarios[i][0] + scenarios[i][3] * scenarios[i][1]) for i in range(len(scenarios))])
        cost_expr = company.cost.fixed_cost + prod * (company.cost.total_unit_cost()) + inv_end * (company.cost.inventory_holding_cost)

        model += revenue_expr - cost_expr

        # Solve the model
        model.solve()

        # Find chosen scenario
        chosen = None
        for i in x:
            if x[i].varValue > 0.5:
                chosen = i
                break

        if chosen is not None:
            pe, pl, dA_early, dA_lm = scenarios[chosen]
            chosen_prod = prod.varValue
            chosen_inv = inv_end.varValue
            profit = revenue_expr.value() - cost_expr.value()
            return pe, pl, chosen_prod, chosen_inv, profit, dA_early, dA_lm
        else:
            # Fallback falls kein Szenario gewählt wird
            return company.base_price, 100, 0, company.inventory, 0, 0, 0


class StrategyStatic:
    """
    Einfache, adaptive Strategie für Unternehmen B:
    Passt den Preis leicht an basierend auf der Konkurrenz.
    """
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
