
import numpy as np

class TokenScorer:
    def __init__(self):
        self.liq_weight = 1.1
        self.holder_weight = 0.3
        self.sentiment_weight = 0.9

    def score(self, token):
        liq = token.get("liquidity", 0)
        holders = token.get("holders", 1)
        sentiment = token.get("sentiment", 0.5)
        adjusted = np.log1p(liq) * (holders ** self.holder_weight) * sentiment * self.liq_weight
        risk_penalty = 0.05 if token.get("is_flagged") else 0
        return round(adjusted * self.sentiment_weight - risk_penalty, 4)
