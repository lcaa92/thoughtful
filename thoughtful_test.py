import unittest
from thoughtful import sort

class TestSortFunction(unittest.TestCase):
    def test_standard_package(self):
        # Not bulky, not heavy
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")
    
    def test_bulky_by_volume(self):
        # Bulky by volume (width * height * length >= 1,000,000)
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")
    
    def test_bulky_by_dimension(self):
        # Bulky by dimension (one dimension >= 150)
        self.assertEqual(sort(151, 10, 10, 10), "SPECIAL")
        self.assertEqual(sort(10, 151, 10, 10), "SPECIAL")
        self.assertEqual(sort(10, 10, 151, 10), "SPECIAL")
    
    def test_heavy(self):
        # Heavy (mass >= 20)
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
        self.assertEqual(sort(10, 10, 10, 25), "SPECIAL")
    
    def test_rejected_bulky_and_heavy(self):
        # Both bulky and heavy
        self.assertEqual(sort(151, 10, 10, 25), "REJECTED")
        self.assertEqual(sort(100, 100, 100, 25), "REJECTED")
    
    def test_edge_cases(self):
        # Edge case: exactly at the limits
        self.assertEqual(sort(100, 100, 100, 19), "SPECIAL")
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")
        self.assertEqual(sort(150, 10, 10, 19), "SPECIAL")
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")
        self.assertEqual(sort(10, 10, 10, 19), "STANDARD")
    
    def test_zero_and_negative_values(self):
        # Zero and negative values (should be STANDARD unless mass >= 20)
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")
        self.assertEqual(sort(-10, -10, -10, -5), "STANDARD")
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")
        self.assertEqual(sort(151, 10, 10, 20), "REJECTED")

if __name__ == "__main__":
    unittest.main()