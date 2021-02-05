import unittest
import listAverage

class volumeTest(unittest.TestCase):
    def test_logic(self):
        myList = [2, 4, 6, 8]
        self.assertEqual(listAverage.findAverage(myList), 5)
    
    def test_float(self):
        myList = [1.2, 1.2, 1.4, 1]
        self.assertEqual(listAverage.findAverage(myList), 1.2)

    def test_string(self):
        myList = ["fruit", 4, 6, "cars"]
        self.assertIsInstance(listAverage.findAverage(myList), int)

if __name__ == "__main__":
    unittest.main(verbosity = 2)
