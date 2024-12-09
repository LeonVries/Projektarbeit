class Company:
    """
    Stufe 2 Unternehmen:
    - Hält Preis und Kostenstruktur
    - Gewinn: π = (p - c)*Q
    """
    def __init__(self, name, cost, initial_price):
        self.name = name
        self.cost = cost
        self.price = initial_price

    def set_price(self, price):
        self.price = price

    def profit(self, quantity):
        return (self.price - self.cost.get_marginal_cost()) * quantity
