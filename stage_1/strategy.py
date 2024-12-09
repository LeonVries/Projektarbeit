import numpy as np

class BertrandUnderbiddingStrategy:
    """
    Strategie für Stufe 2:
    - Wenn eigenes Unternehmen teurer ist als das andere, unterbietet es den Preis des anderen
      um bis zu max_underbid Prozent.
    - Sonst bleibt der Preis konstant.
    """
    def __init__(self, max_underbid=0.08):
        self.max_underbid = max_underbid

    def adjust_price(self, own_price, competitor_price, marginal_cost):
        if own_price > competitor_price:
            # Unterbiete den Konkurrenten
            factor = 1 - np.random.uniform(0, self.max_underbid)
            new_price = max(marginal_cost, competitor_price * factor)
            return new_price
        else:
            # Evtl. ist man bereits günstiger oder gleich teuer
            factor = 1 - np.random.uniform(0, self.max_underbid)
            new_price = max(marginal_cost, own_price * factor) if own_price >= competitor_price else own_price
            return new_price
