import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="src/alert/alerts.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_alert(vulnerability_type, details, severity="Medium"):
    """
    Logs an alert to alerts.log with details about the detected vulnerability.

    Args:
        vulnerability_type (str): The type of vulnerability detected (e.g., "Buffer Overflow").
        details (str): Additional information about the vulnerability.
        severity (str): The severity of the alert (e.g., "Critical", "High", "Medium", "Low").
    """
    alert_message = f"Vulnerability Detected: {vulnerability_type} | Severity: {severity} | Details: {details}"
    logging.info(alert_message)
    print(f"[ALERT] {alert_message}")

if __name__ == "__main__":
    # Example usage of log_alert function
    log_alert("Buffer Overflow", "Detected in vulnerable_function() while processing user input.", "High")
    log_alert("Trapdoor", "Unauthorized privilege escalation detected in system logs.", "Critical")
