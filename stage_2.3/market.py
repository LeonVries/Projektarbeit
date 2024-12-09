import numpy as np

class Market:
    def __init__(self, 
                 early_price_sensitivity=3.0, 
                 last_minute_base_sensitivity=1.0, 
                 early_ratio=0.8, 
                 last_minute_ratio=0.2,
                 market_size_mean=1000,
                 market_size_std=200,
                 random_seed=42):
        np.random.seed(random_seed)
        self.early_price_sensitivity = early_price_sensitivity
        self.last_minute_base_sensitivity = last_minute_base_sensitivity
        self.early_ratio = early_ratio
        self.last_minute_ratio = last_minute_ratio
        self.market_size_mean = market_size_mean
        self.market_size_std = market_size_std

    def market_share(self, price_A, price_B, sensitivity):
        price_diff = (price_B - price_A) / ((price_A + price_B)/2 + 1e-9)
        share_A = 1 / (1 + np.exp(-sensitivity * price_diff))
        share_B = 1 - share_A
        return share_A, share_B

    def generate_demands(self, price_A_early, price_B_early, price_A_last, price_B_last):
        base_market = np.random.normal(self.market_size_mean, self.market_size_std)
        base_market = max(0, base_market)

        avg_price_early = (price_A_early + price_B_early) / 2
        early_factor = 1 - max(0, (avg_price_early - 100) * 0.003)
        early_factor = np.clip(early_factor, 0.3, 1.0)
        early_demand_total = base_market * self.early_ratio * early_factor

        avg_price_last = (price_A_last + price_B_last) / 2
        if avg_price_last < 100:
            lm_boost = 1 + (100 - avg_price_last) * 0.01
        else:
            lm_boost = 1 - (avg_price_last - 100) * 0.002
        lm_boost = np.clip(lm_boost, 0.5, 1.5)

        last_minute_base = base_market * self.last_minute_ratio
        last_minute_demand_total = max(0, np.random.normal(last_minute_base * lm_boost,
                                                           last_minute_base * lm_boost * 0.3))

        share_A_early, share_B_early = self.market_share(price_A_early, price_B_early, self.early_price_sensitivity)
        share_A_lm, share_B_lm = self.market_share(price_A_last, price_B_last, self.last_minute_base_sensitivity)

        dA_early = share_A_early * early_demand_total
        dB_early = share_B_early * early_demand_total
        dA_lm = share_A_lm * last_minute_demand_total
        dB_lm = share_B_lm * last_minute_demand_total

        return dA_early, dA_lm, dB_early, dB_lm
