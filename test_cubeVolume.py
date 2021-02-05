import unittest
import cubeVolume

class volumeTest(unittest.TestCase):
    def test_logic(self):
        self.assertEqual(cubeVolume.findVolume(2, 3, 4), 24)
    
    def test_float(self):
        self.assertEqual(cubeVolume.findVolume(0.5, 10, 1), 5)

    def test_string(self):
        self.assertIsInstance(cubeVolume.findVolume("asdf", 10, 1), int)

if __name__ == "__main__":
    unittest.main(verbosity = 2)
