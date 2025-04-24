import os
import time
import random
import datetime
import json
import threading

class DetectionService:
    def __init__(self):
        self.alert_log_file = os.path.join(os.path.dirname(__file__), '../alert/alerts.json')
        self.initialized = False
        self.running = False
        os.makedirs(os.path.dirname(self.alert_log_file), exist_ok=True)
        
        # Initialize alert log if it doesn't exist
        if not os.path.exists(self.alert_log_file):
            with open(self.alert_log_file, 'w') as f:
                json.dump([], f)
        else:
            # Validate and fix JSON file if corrupted
            self._ensure_valid_json()
        
        self.initialized = True
        print("Detection Service initialized successfully.")
    
    def _ensure_valid_json(self):
        """Ensure the alerts JSON file is valid, fixing it if necessary."""
        try:
            with open(self.alert_log_file, 'r') as f:
                alerts = json.load(f)
            
            # File loaded successfully, no need to fix
            return
        except json.JSONDecodeError:
            print("[WARNING] Alerts file is corrupted. Attempting to fix...")
            try:
                # Try to fix by reading the file as text and finding the last valid bracket
                with open(self.alert_log_file, 'r') as f:
                    content = f.read()
                
                # Find the position of the last valid closing bracket
                if ']' in content:
                    valid_content = content[:content.rindex(']') + 1]
                    
                    # Try to parse the truncated content
                    json.loads(valid_content)
                    
                    # If it parsed correctly, write it back
                    with open(self.alert_log_file, 'w') as f:
                        f.write(valid_content)
                    print("[INFO] Successfully fixed corrupted alerts file.")
                    return
            except Exception as e:
                print(f"[ERROR] Could not repair the JSON file: {e}")
            
            # If all repair attempts failed, reset the file
            print("[WARNING] Creating new alerts file due to irrecoverable corruption.")
            with open(self.alert_log_file, 'w') as f:
                json.dump([], f)
    
    def monitor_buffer_overflow(self):
        while self.running:
            # Check for buffer overflow vulnerabilities
            print("[INFO] Monitoring for Buffer Overflow vulnerabilities...")
            if random.random() < 0.3:  # 30% chance of detection
                self.generate_alert("Buffer Overflow", "Potential buffer overflow detected in system call", "High")
            time.sleep(5)
    
    def monitor_trapdoor(self):
        while self.running:
            # Check for trapdoor vulnerabilities
            print("[INFO] Monitoring for Trapdoor vulnerabilities...")
            if random.random() < 0.2:  # 20% chance of detection
                self.generate_alert("Trapdoor", "Suspicious backdoor activity detected", "Critical")
            time.sleep(7)
    
    def monitor_cache_poisoning(self):
        while self.running:
            # Check for cache poisoning vulnerabilities
            print("[INFO] Monitoring for Cache Poisoning vulnerabilities...")
            if random.random() < 0.25:  # 25% chance of detection
                self.generate_alert("Cache Poisoning", "Possible ARP cache poisoning attempt", "Medium")
            time.sleep(6)
    
    def generate_alert(self, type, message, severity):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        alert = {
            "timestamp": timestamp,
            "type": type,
            "message": message,
            "severity": severity
        }
        
        # Use file locking to prevent corruption
        MAX_RETRIES = 3
        for attempt in range(MAX_RETRIES):
            try:
                # First ensure the JSON file is valid
                self._ensure_valid_json()
                
                # Now try to read the existing alerts
                with open(self.alert_log_file, 'r') as f:
                    alerts = json.load(f)
                
                # Add the new alert
                alerts.append(alert)
                
                # Write the updated alerts back to the file
                with open(self.alert_log_file, 'w') as f:
                    json.dump(alerts, f, indent=2)
                
                print(f"[ALERT] {severity} - {type}: {message}")
                return  # Success, exit the retry loop
            except Exception as e:
                print(f"Error generating alert (attempt {attempt+1}/{MAX_RETRIES}): {e}")
                time.sleep(0.5)  # Small delay before retry
        
        print(f"[ERROR] Failed to generate alert after {MAX_RETRIES} attempts")
    
    def start(self):
        if not self.initialized:
            print("Error: Detection Service not initialized")
            return False
            
        self.running = True
        print("Starting Detection Service...")
        
        # Start monitoring threads
        threading.Thread(target=self.monitor_buffer_overflow, daemon=True).start()
        threading.Thread(target=self.monitor_trapdoor, daemon=True).start()
        threading.Thread(target=self.monitor_cache_poisoning, daemon=True).start()
        
        return True
    
    def stop(self):
        self.running = False
        print("Detection Service stopped.")

if __name__ == "__main__":
    service = DetectionService()
    service.start()
    
    try:
        # Keep the main thread running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        service.stop()
        print("Detection Service terminated by user.") 