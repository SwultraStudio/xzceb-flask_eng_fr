import unittest

from translator import english_to_french
from translator import french_to_english

class Translation_Tests(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french(),'')

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')

    def test_french_to_english(self):
        self.assertEqual(french_to_english(),'')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')