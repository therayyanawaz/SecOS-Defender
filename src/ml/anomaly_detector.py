# Example pseudocode for ML-based detection
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.01)
    
    def train(self, normal_data):
        self.model.fit(normal_data)
    
    def detect(self, current_data):
        return self.model.predict(current_data)
