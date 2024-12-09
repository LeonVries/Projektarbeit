class Company:
    """
    Modelliert ein Unternehmen mit linearen Reaktionsfunktionen.
    """
    def __init__(self, alpha, beta, gamma, marginal_cost, name):
        self.alpha = alpha  # Basis-Nachfrageparameter
        self.beta = beta    # Eigene Preisempfindlichkeit
        self.gamma = gamma  # Kreuzpreisempfindlichkeit
        self.marginal_cost = marginal_cost
        self.name = name

    def reaction_price(self, competitor_price):
        """Berechnet den optimalen Preis als Reaktion auf den Preis des Konkurrenten."""
        return (self.alpha + self.beta * self.marginal_cost + self.gamma * competitor_price) / (2 * self.beta)