def detect_trapdoor():
    """
    Detects potential trapdoors by scanning for unauthorized privilege escalations.
    """
    suspicious_patterns = ["sudo", "su", "chmod 777"]
    detected = []

    # Simulate scanning system logs for suspicious commands
    try:
        with open("system_logs.txt", "r") as logs:
            for line in logs:
                for pattern in suspicious_patterns:
                    if pattern in line:
                        detected.append(line.strip())
    except FileNotFoundError:
        print("[ERROR] system_logs.txt not found. Please provide the log file.")
        return

    if detected:
        print("[ALERT] Trapdoor detected:")
        for entry in detected:
            print(f" - {entry}")
    else:
        print("No trapdoors detected.")

if __name__ == "__main__":
    detect_trapdoor()
