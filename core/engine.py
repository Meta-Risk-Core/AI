
import logging
from analytics.token_scorer import TokenScorer
from wallets.wallet_profiler import WalletProfiler
from risklab.rug_detector import RugDetector

class Engine:
    def __init__(self):
        self.scorer = TokenScorer()
        self.profiler = WalletProfiler()
        self.risk = RugDetector()

    def analyze_wallet(self, wallet):
        tokens = self.profiler.get_tokens(wallet)
        results = []
        for token in tokens:
            score = self.scorer.score(token)
            rug_risk = self.risk.estimate(token)
            results.append({
                "symbol": token.get("symbol"),
                "score": score,
                "rug_risk": rug_risk
            })
        results.sort(key=lambda x: (-x["score"], x["rug_risk"]))
        return results
