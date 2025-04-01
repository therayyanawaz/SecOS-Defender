import unittest
from src.simulation.attack_simulator import simulate_buffer_overflow, simulate_trapdoor, simulate_cache_poisoning

class TestSimulationEngine(unittest.TestCase):

    def test_buffer_overflow_simulation(self):
        """
        Tests the buffer overflow simulation.
        """
        try:
            simulate_buffer_overflow()
            simulated = True
        except Exception as e:
            simulated = False
        self.assertTrue(simulated, "Buffer overflow simulation failed.")

    def test_trapdoor_simulation(self):
        """
        Tests the trapdoor simulation.
        """
        try:
            simulate_trapdoor()
            simulated = True
        except Exception as e:
            simulated = False
        self.assertTrue(simulated, "Trapdoor simulation failed.")

    def test_cache_poisoning_simulation(self):
        """
        Tests the cache poisoning simulation.
        """
        try:
            simulate_cache_poisoning()
            simulated = True
        except Exception as e:
            simulated = False
        self.assertTrue(simulated, "Cache poisoning simulation failed.")

if __name__ == "__main__":
    unittest.main()
