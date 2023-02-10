import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"),"Bonjour") 
        self.assertNotEqual(englishToFrench("Hello"),None)
        

class TestFranch(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello") 
        self.assertNotEqual(frenchToEnglish("Bonjour"),None)
unittest.main()