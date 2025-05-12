
class RugDetector:
    def __init__(self):
        self.flag_threshold = 0.2

    def estimate(self, token):
        liq = token.get("liquidity", 0)
        holders = token.get("holders", 1)
        sentiment = token.get("sentiment", 0.5)
        base_risk = 1.0 - (liq / (liq + 50000)) * (holders / (holders + 100)) * sentiment
        if token.get("is_flagged"):
            base_risk += 0.15
        return round(min(base_risk, 1.0), 3)
