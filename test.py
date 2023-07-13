
import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("hello"),"bonjour")
        self.assertEqual(englishToFrench("welcome"),"bienvenue")
        self.assertEqual(englishToFrench("love"),"Amour")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("bonjour"),"hello")
        self.assertEqual(frenchToEnglish("bienvenue"),"welcome")
        self.assertEqual(frenchToEnglish("Amour"),"love")

unittest.main()