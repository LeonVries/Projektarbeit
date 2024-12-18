import numpy as np


#Hier dzt. nur fixe kosten; Allgmeine Variable Kosten und explizit als Bsp. noch einmal Materialpreise die ebenfalls alle schwanken
#Möglichkeit zb Rohstoffknappheit zu ergänzen, oder Lieferanten Kappa limitieren
#Ebenfalls Krisen integrierbar


# cost.py

class Cost:
    def __init__(self, fixed_cost, marginal_cost, raw_material_price, inventory_holding_cost):
        self.fixed_cost = fixed_cost
        self.marginal_cost = marginal_cost
        self.raw_material_price = raw_material_price
        self.inventory_holding_cost = inventory_holding_cost

    def total_unit_cost(self):
        return self.marginal_cost + self.raw_material_price

    def update_fixed_costs(self, inflation_rate=0.01):
        self.fixed_cost *= (1 + inflation_rate * 0.1)

    def update_marginal_costs(self, fluctuation_std=0.05):
        fluctuation = np.random.normal(0, fluctuation_std)
        self.marginal_cost *= (1 + fluctuation)
        self.marginal_cost = max(1, self.marginal_cost)

    def update_raw_material_price(self, fluctuation_std=0.15):
        fluctuation = np.random.normal(0, fluctuation_std)
        self.raw_material_price *= (1 + fluctuation)
        self.raw_material_price = max(1, self.raw_material_price)

    def get_marginal_cost(self):
        return self.marginal_cost

