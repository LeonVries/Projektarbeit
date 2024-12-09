import numpy as np

class Market:
    """
    Stufe 2 Markt:
    - Einfaches Bertrand-Modell mit linearem Nachfrageverhalten
    - Marktnachfrage: Q = Marktgröße * (1 - p/max_price), falls p < max_price sonst 0
    - Marktanteil über logistische Funktion abhängig vom Preisunterschied
    """
    def __init__(self, market_size, max_price, price_sensitivity=2.0):
        self.market_size = market_size
        self.max_price = max_price
        self.price_sensitivity = price_sensitivity

    def market_share(self, price_a, price_b):
        if price_a >= self.max_price or price_b >= self.max_price:
            return 0.5, 0.5  # Bei sehr hohem Preis aller negativ
        # Logistische Funktion
        price_diff = (price_b - price_a) / ((price_a + price_b)/2 + 1e-9)
        share_a = 1 / (1 + np.exp(-self.price_sensitivity * price_diff))
        share_b = 1 - share_a
        return share_a, share_b

    def demand(self, price):
        return max(0, self.market_size * (1 - price/self.max_price))
