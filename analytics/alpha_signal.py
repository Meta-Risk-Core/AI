
import pandas as pd
import numpy as np

class AlphaSignal:
    def __init__(self):
        self.weights = np.random.rand(5)
        self.bias = np.random.rand()

    def normalize(self, df):
        return (df - df.min()) / (df.max() - df.min() + 1e-5)

    def score_row(self, row):
        return np.dot(row.values[:5], self.weights) + self.bias

    def evaluate_frame(self, frame):
        frame = self.normalize(frame)
        frame["score"] = frame.apply(self.score_row, axis=1)
        return frame.sort_values("score", ascending=False)
