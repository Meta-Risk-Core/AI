
import random

class WalletProfiler:
    def get_tokens(self, wallet):
        token_count = random.randint(2, 5)
        result = []
        for i in range(token_count):
            result.append({
                "symbol": f"COIN{i}",
                "liquidity": random.uniform(10000, 80000),
                "holders": random.randint(50, 500),
                "sentiment": round(random.uniform(0.3, 0.95), 2),
                "is_flagged": random.choice([True, False])
            })
        return result
