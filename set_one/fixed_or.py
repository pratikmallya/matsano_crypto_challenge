"""
Given two buffers of equal length, produce their XOR.
Python can do bitwise XOR only on integers, so you have to
convert into integers and then do the XOR
"""

import unittest


class TestAlg(unittest.TestCase):

    def test_1(self):
        i1 = '1c0111001f010100061a024b53535009181c'
        i2 = '686974207468652062756c6c277320657965'
        res = '746865206b696420646f6e277420706c6179'
        self.assertEqual(fixed_or(i1, i2), res)


def fixed_or(num1, num2):
    """Compute OR of two hex numbers

    Args:
        num1, num2: 2 strings in hex
    """
    int_num1 = int(num1, 16)
    int_num2 = int(num2, 16)

    return hex(int_num1 ^ int_num2)[2:]


if __name__ == "__main__":
    unittest.main()
