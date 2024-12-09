from pulp import LpProblem, LpMaximize, LpVariable, lpSum

class CompanyDynamic:
    def __init__(self, name, capacity, cost, base_price, inventory=0):
        self.name = name
        self.capacity = capacity
        self.cost = cost
        self.base_price = base_price
        self.inventory = inventory
        self.last_decision = None
        self.buffer_stock = 20

    def set_buffer_stock(self, new_buffer):
        self.buffer_stock = new_buffer

    def use_strategy(self, strategy, price_B_early, price_B_last, market):
        # Strategie aufrufen, um die optimale Entscheidung zu treffen
        result = strategy.optimize_decision(self, price_B_early, price_B_last, market)
        # result = (pe, pl, prodA, invA, profit, dA_early, dA_lm)
        self.last_decision = result
        pe, pl, prodA, invA, profit, dA_early, dA_lm = result
        self.inventory = invA
        self.base_price = pe


class CompanyStatic:
    def __init__(self, name, capacity, cost, base_price):
        self.name = name
        self.capacity = capacity
        self.cost = cost
        self.base_price = base_price

    def simple_decision(self, dB_early, dB_lm):
        prod = min(self.capacity, dB_early + dB_lm)
        cost_val = self.cost.fixed_cost + prod * (self.cost.total_unit_cost())
        sold = min(prod, dB_early + dB_lm)
        revenue = sold * self.base_price
        profit = revenue - cost_val
        return profit, sold

    def adjust_price(self, strategy, competitor_price):
        # Strategie für B aufrufen, um den Preis anzupassen
        new_price = strategy.adjust_price(self.base_price, competitor_price, self.cost.get_marginal_cost())
        self.base_price = new_price
