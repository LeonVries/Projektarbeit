class Cost:
    """
    Einfache Kostenstruktur für Stufe 2:
    - Marginal Cost (Grenzkosten) als Konstante
    - Keine Lagerkosten, keine Fixkosten-Fluktuation
    """
    def __init__(self, marginal_cost):
        self.marginal_cost = marginal_cost

    def get_marginal_cost(self):
        return self.marginal_cost
