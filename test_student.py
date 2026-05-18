import unittest
from proj3 import huffman_encoding

class TestHuffmanEncoding(unittest.TestCase):
    def test_bayou(self):
        input_string = "bayou"
        expected_encoded = "111110100001"
        expected_codes = {'o': '00', 'u': '01', 'y': '10', 'a': '110', 'b': '111'}
        encoded, decoded, codes = huffman_encoding(input_string)
        self.assertEqual(encoded, expected_encoded)
        self.assertEqual(decoded, input_string)
        self.assertEqual(codes, expected_codes)

    def test_chicago(self):
        input_string = "chicago"
        expected_encoded = "101101111001001100"
        expected_codes = {'o': '00', 'a': '010', 'g': '011', 'c': '10', 'h': '110', 'i': '111'}
        encoded, decoded, codes = huffman_encoding(input_string)
        self.assertEqual(encoded, expected_encoded)
        self.assertEqual(decoded, input_string)
        self.assertEqual(codes, expected_codes)

    def test_cheetah(self):
        input_string = "cheetah"
        expected_encoded = "0111110100001011"
        expected_codes = {'t': '00', 'a': '010', 'c': '011', 'e': '10', 'h': '11'}
        encoded, decoded, codes = huffman_encoding(input_string)
        self.assertEqual(encoded, expected_encoded)
        self.assertEqual(decoded, input_string)
        self.assertEqual(codes, expected_codes)

    def test_ATL(self):
        input_string = "ATL"
        expected_encoded = "10011"
        expected_codes = {'T': '0', 'A': '10', 'L': '11'}
        encoded, decoded, codes = huffman_encoding(input_string)
        self.assertEqual(encoded, expected_encoded)
        self.assertEqual(decoded, input_string)
        self.assertEqual(codes, expected_codes)

if __name__ == "__main__":
    unittest.main()


