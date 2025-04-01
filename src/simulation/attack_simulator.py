import os
import time

def simulate_buffer_overflow():
    """
    Simulates a buffer overflow by running the vulnerable C program.
    """
    print("[INFO] Simulating Buffer Overflow...")
    os.system("gcc -fsanitize=address -o buffer_overflow src/detection/buffer_overflow.c")
    os.system("./buffer_overflow AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")  # Input exceeding buffer size
    print("[INFO] Buffer Overflow simulation complete.\n")


def simulate_trapdoor():
    """
    Simulates a trapdoor by adding suspicious commands to system logs.
    """
    print("[INFO] Simulating Trapdoor...")
    with open("system_logs.txt", "a") as log_file:
        log_file.write("user1 ran sudo chmod 777 /etc/passwd\n")
        log_file.write("user2 executed su root\n")
    print("[INFO] Trapdoor simulation complete. Logs updated.\n")


def simulate_cache_poisoning():
    """
    Simulates ARP cache poisoning by adding suspicious entries to ARP traffic logs.
    """
    print("[INFO] Simulating Cache Poisoning...")
    with open("arp_traffic_logs.txt", "a") as log_file:
        log_file.write("unsolicited ARP reply from 192.168.1.5\n")
        log_file.write("duplicate IP detected for 192.168.1.10\n")
    print("[INFO] Cache Poisoning simulation complete. Logs updated.\n")


if __name__ == "__main__":
    print("Starting Attack Simulation Engine...\n")
    
    # Simulate each attack type with delays
    simulate_buffer_overflow()
    time.sleep(2)
    
    simulate_trapdoor()
    time.sleep(2)
    
    simulate_cache_poisoning()
    time.sleep(2)
    
    print("All attack simulations completed.")
