"""
Convert a stream of hex numbers to base64

So, this took me an extrordinary amount of time to solve. Why? I assumed that
the encoded string was an integer! Why would I think that?? I guess there are
just some hardcoded assumptions in my brain which I need to be vary of.
However, it did make for some interesting reading on bytearrays in Python

So, the answer to this problem is ridiculously easy in Python: use the
base64 module
"""

from base64 import b16decode, b64encode
import unittest


class TestAlg(unittest.TestCase):

    def test_1(self):
        v = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        v64 = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        self.assertEqual(hex_to_64(v), v64)


def hex_to_64(hexvalue):
    """convert from hex to base64"""
    return b64encode(b16decode(hexvalue.upper()))


if __name__ == "__main__":
    unittest.main()