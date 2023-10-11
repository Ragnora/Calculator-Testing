import unittest
from unittest.mock import patch
from kalkulator import calculator

class TestCalculator(unittest.TestCase):

    #Penjumlahan
    @patch('builtins.input', side_effect=["1","7","3"])
    def testPenjumlahan(self, mock_inputs):
        result = calculator()
        self.assertEqual(result, 10)
    
    #Pengurangan
    @patch('builtins.input', side_effect=["2","10","5"])
    def testPengurangan(self, mock_inputs):
        result = calculator()
        self.assertEqual(result, 5)

    #Perkalian
    @patch('builtins.input', side_effect=["3","6","3"])
    def testPerkalian(self, mock_inputs):
        result = calculator()
        self.assertEqual(result, 18)

    #Pembagian
    @patch('builtins.input', side_effect=["4","8","4"])
    def testPembagian(self, mock_inputs):
        result = calculator()
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()

    