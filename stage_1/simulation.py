import matplotlib.pyplot as plt
import numpy as np

class Simulation:
    """
    Simulation für Stufe 2:
    - Zwei Unternehmen im Bertrand-Wettbewerb
    - Jedes Unternehmen wendet die BertrandUnderbiddingStrategy an
    - Simuliert über num_periods Perioden
    """
    def __init__(self, market, company_a, company_b, strategy_a, strategy_b, num_periods=50):
        self.market = market
        self.company_a = company_a
        self.company_b = company_b
        self.strategy_a = strategy_a
        self.strategy_b = strategy_b
        self.num_periods = num_periods

    def run(self):
        prices_a = np.zeros(self.num_periods)
        prices_b = np.zeros(self.num_periods)
        profits_a = np.zeros(self.num_periods)
        profits_b = np.zeros(self.num_periods)
        shares_a = np.zeros(self.num_periods)
        shares_b = np.zeros(self.num_periods)

        prices_a[0] = self.company_a.price
        prices_b[0] = self.company_b.price

        for t in range(self.num_periods - 1):
            # Marktanteile
            share_a, share_b = self.market.market_share(prices_a[t], prices_b[t])
            Q_total = self.market.demand((prices_a[t] + prices_b[t])/2)
            Qa = Q_total * share_a
            Qb = Q_total * share_b

            profits_a[t] = self.company_a.profit(Qa)
            profits_b[t] = self.company_b.profit(Qb)
            shares_a[t] = share_a
            shares_b[t] = share_b

            # Preisupdate:
            new_price_a = self.strategy_a.adjust_price(prices_a[t], prices_b[t], self.company_a.cost.get_marginal_cost())
            new_price_b = self.strategy_b.adjust_price(prices_b[t], prices_a[t], self.company_b.cost.get_marginal_cost())

            prices_a[t+1] = new_price_a
            prices_b[t+1] = new_price_b

        # Letzte Periode noch berechnen
        share_a, share_b = self.market.market_share(prices_a[-1], prices_b[-1])
        Q_total = self.market.demand((prices_a[-1] + prices_b[-1])/2)
        Qa = Q_total * share_a
        Qb = Q_total * share_b
        profits_a[-1] = self.company_a.profit(Qa)
        profits_b[-1] = self.company_b.profit(Qb)
        shares_a[-1] = share_a
        shares_b[-1] = share_b

        return prices_a, prices_b, profits_a, profits_b, shares_a, shares_b

    def plot_results(self, prices_a, prices_b, profits_a, profits_b, shares_a, shares_b):
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

        # Preise
        ax1.plot(prices_a, label='Unternehmen A')
        ax1.plot(prices_b, label='Unternehmen B')
        ax1.set_title('Preisentwicklung')
        ax1.set_ylabel('Preis')
        ax1.legend()

        # Gewinne
        ax2.plot(profits_a, label='Unternehmen A')
        ax2.plot(profits_b, label='Unternehmen B')
        ax2.set_title('Gewinnentwicklung')
        ax2.set_ylabel('Gewinn')
        ax2.legend()

        # Marktanteile
        ax3.plot(shares_a, label='Unternehmen A')
        ax3.plot(shares_b, label='Unternehmen B')
        ax3.set_title('Marktanteilsentwicklung')
        ax3.set_ylabel('Marktanteil')
        ax3.set_xlabel('Periode')
        ax3.legend()

        plt.tight_layout()
        plt.show()

# Beispielhafter Lauf (Stufe 2)
if __name__ == "__main__":
    from cost import Cost
    from market import Market
    from company import Company
    from strategy import BertrandUnderbiddingStrategy

    c = Cost(marginal_cost=10)
    m = Market(market_size=1000, max_price=50, price_sensitivity=2.0)
    A = Company(name='A', cost=c, initial_price=45)
    B = Company(name='B', cost=c, initial_price=40)
    stratA = BertrandUnderbiddingStrategy()
    stratB = BertrandUnderbiddingStrategy()

    sim = Simulation(m, A, B, stratA, stratB, num_periods=50)
    pA, pB, piA, piB, sA, sB = sim.run()
    sim.plot_results(pA, pB, piA, piB, sA, sB)
