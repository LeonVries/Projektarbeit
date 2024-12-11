from pulp import LpProblem, LpMaximize, LpVariable, lpSum
import numpy as np

# Firma A Dynamisch 
class CompanyDynamic:
    def __init__(self, name, capacity, cost, base_price, inventory=0, buffer_stock=20, demand_uncertainty=0.1):
        self.name = name
        self.capacity = capacity
        self.cost = cost
        self.base_price = base_price
        self.inventory = inventory
        self.last_decision = None
        self.buffer_stock = buffer_stock
        self.demand_uncertainty = demand_uncertainty  # 10% Unsicherheit standardmäßig

    def set_buffer_stock(self, new_buffer):
        self.buffer_stock = new_buffer

    def use_strategy(self, strategy, price_B_early, price_B_last, market):
        # Strategie aufrufen, um die optimale Entscheidung zu treffen
        result = strategy.optimize_decision(self, price_B_early, price_B_last, market)
        # result = (pe, pl, prodA, invA, profit, dA_early_est, dA_lm_est)
        self.last_decision = result
        pe, pl, prodA, invA, profit, dA_early_est, dA_lm_est = result
        self.inventory = invA
        self.base_price = pe

# Firma B statisch (Aktualisiert zur Berücksichtigung von Nachfrageschwankungen)
# company.py

class CompanyStatic:
    def __init__(self, name, capacity, cost, base_price, inventory=0, buffer_stock=20, demand_uncertainty=0.1):
        self.name = name
        self.capacity = capacity
        self.cost = cost
        self.base_price = base_price
        self.inventory = inventory
        self.buffer_stock = buffer_stock
        self.demand_uncertainty = demand_uncertainty

    def simple_decision(self, actual_dB_early, actual_dB_lm):
        # Nachfrageabschätzung mit Unsicherheit
        uncertainty_factor_early = np.random.uniform(1 - self.demand_uncertainty, 1 + self.demand_uncertainty)
        uncertainty_factor_lm = np.random.uniform(1 - self.demand_uncertainty, 1 + self.demand_uncertainty)

        dB_early_est = actual_dB_early * uncertainty_factor_early
        dB_lm_est = actual_dB_lm * uncertainty_factor_lm

        # Produktionsentscheidung basierend auf geschätzter Nachfrage und Pufferbestand
        desired_inventory = self.buffer_stock
        production = min(self.capacity, dB_early_est + dB_lm_est + desired_inventory - self.inventory)

        # Verfügbare Menge (Produktion + Inventar)
        available = production + self.inventory

        # Tatsächliche Verkäufe sind das Minimum aus verfügbarer Menge und tatsächlicher Nachfrage
        sales = min(available, actual_dB_early + actual_dB_lm)

        # Aktualisierung des Inventars
        new_inventory = available - sales
        self.inventory = new_inventory

        # Berechnung der Einnahmen
        revenue = sales * self.base_price

        # Berechnung der Kosten: Fixkosten + variable Produktionskosten + Lagerhaltungskosten
        cost_var = production * self.cost.total_unit_cost()
        cost_fixed = self.cost.fixed_cost
        cost_holding = new_inventory * self.cost.inventory_holding_cost
        total_cost = cost_fixed + cost_var + cost_holding

        # Berechnung des Gewinns
        profit = revenue - total_cost

        return profit, production, sales

    def adjust_price(self, strategy, competitor_price):
        # Strategie für B aufrufen, um den Preis anzupassen
        new_price = strategy.adjust_price(self.base_price, competitor_price, self.cost.get_marginal_cost())
        self.base_price = new_price
