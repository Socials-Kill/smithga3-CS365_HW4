import unittest
import nameGenerator

class nameTest(unittest.TestCase):
    def test_logic(self):
        self.assertEqual(nameGenerator.makeName("Firstname", "Lastname"), "Firstname Lastname")
    
    def test_specialChar(self):
        self.assertEqual(nameGenerator.makeName("Ä路边", "æ"), "Ä路边 æ")

    def test_mixedInput(self):
        self.assertEqual(nameGenerator.makeName("Firstname", 3), "Firstname 3")

if __name__ == "__main__":
    unittest.main(verbosity = 2)
