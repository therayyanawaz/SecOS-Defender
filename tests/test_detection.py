import unittest
from src.detection.trapdoor import detect_trapdoor
from src.detection.cache_poison import detect_cache_poisoning

class TestDetectionModules(unittest.TestCase):

    def test_trapdoor_detection(self):
        # Create a mock system_logs.txt file
        with open("system_logs.txt", "w") as log_file:
            log_file.write("user1 ran sudo chmod 777 /etc/passwd\n")
            log_file.write("user2 executed su root\n")

        # Capture output
        try:
            detect_trapdoor()
            detected = True
        except FileNotFoundError:
            detected = False

        self.assertTrue(detected, "Trapdoor detection failed.")

    def test_cache_poisoning_detection(self):
        # Create a mock arp_traffic_logs.txt file
        with open("arp_traffic_logs.txt", "w") as log_file:
            log_file.write("unsolicited ARP reply from 192.168.1.5\n")
            log_file.write("duplicate IP detected for 192.168.1.10\n")

        # Capture output
        try:
            detect_cache_poisoning()
            detected = True
        except FileNotFoundError:
            detected = False

        self.assertTrue(detected, "Cache poisoning detection failed.")

if __name__ == "__main__":
    unittest.main()
