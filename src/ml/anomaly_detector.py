import numpy as np
from sklearn.ensemble import IsolationForest
from preprocess import SystemMetrics  # Assume metrics collector exists

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.01, random_state=42)
        self.scaler = StandardScaler()
        
    def train(self, normal_metrics):
        scaled = self.scaler.fit_transform(normal_metrics)
        self.model.fit(scaled)
        
    def detect(self, current_metrics):
        return self.model.predict(self.scaler.transform([current_metrics]))
