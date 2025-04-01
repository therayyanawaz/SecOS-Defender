import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class AnomalyDetector:
    def __init__(self):
        """
        Initializes the anomaly detector with an Isolation Forest model.
        """
        self.model = IsolationForest(contamination=0.01, random_state=42)
        self.scaler = StandardScaler()

    def train(self, normal_data):
        """
        Trains the anomaly detector on normal system data.

        Args:
            normal_data (numpy.ndarray): Array of normal system metrics (e.g., CPU usage, memory usage).
        """
        scaled_data = self.scaler.fit_transform(normal_data)
        self.model.fit(scaled_data)
        print("[INFO] Anomaly Detector trained successfully.")

    def detect(self, current_data):
        """
        Detects anomalies in the current system data.

        Args:
            current_data (numpy.ndarray): Array of current system metrics.

        Returns:
            int: 1 if normal, -1 if anomaly detected.
        """
        scaled_data = self.scaler.transform([current_data])
        prediction = self.model.predict(scaled_data)
        return prediction[0]

if __name__ == "__main__":
    # Example usage
    print("[INFO] Initializing Anomaly Detector...")
    detector = AnomalyDetector()

    # Simulated training data (normal metrics: [CPU %, Memory %, Disk %])
    normal_metrics = np.array([
        [10, 20, 30],  # Normal behavior
        [15, 25, 35],
        [12, 22, 32],
        [11, 21, 31],
    ])

    # Train the model
    detector.train(normal_metrics)

    # Simulated current data (system metrics)
    current_metrics = np.array([50, 80, 90])  # Abnormal behavior

    # Detect anomalies
    result = detector.detect(current_metrics)
    if result == -1:
        print("[ALERT] Anomaly detected in system metrics!")
    else:
        print("[INFO] System metrics are normal.")
