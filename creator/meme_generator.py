
import random

class MemeGenerator:
    def __init__(self):
        self.themes = ["wizard", "doge", "pixel frog", "cyber cat", "neon rat"]
        self.adjectives = ["hyper", "meta", "turbo", "quantum", "ultra"]

    def generate_name(self):
        name = f"{random.choice(self.adjectives)}-{random.choice(self.themes)}"
        return name.upper()

    def generate_meta(self):
        return {
            "theme": random.choice(self.themes),
            "adjective": random.choice(self.adjectives),
            "viral_score": round(random.uniform(0.5, 0.99), 3)
        }
