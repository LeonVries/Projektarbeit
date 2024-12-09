import numpy as np
from company import Company

class Market:
    """
    Modelliert den Markt und berechnet das Nash-Gleichgewicht.
    """
    def __init__(self, company1, company2):
        self.company1 = company1
        self.company2 = company2

    def calculate_nash_equilibrium(self):
        """Berechnet das Nash-Gleichgewicht basierend auf den Reaktionsfunktionen."""
        A = np.array([
            [1, -self.company1.gamma / (2 * self.company1.beta)],
            [-self.company2.gamma / (2 * self.company2.beta), 1]
        ])

        b = np.array([
            (self.company1.alpha + self.company1.beta * self.company1.marginal_cost) / (2 * self.company1.beta),
            (self.company2.alpha + self.company2.beta * self.company2.marginal_cost) / (2 * self.company2.beta)
        ])

        prices = np.linalg.solve(A, b)
        return prices