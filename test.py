import cipher_tools
import unittest
class Test(unittest.TestCase):
    def test_affine(self):
        unenc = "hi"
        enc = "BI"
        a = 7
        b=4
        self.assertEqual(cipher_tools.apply_affine_cipher(unenc,a, b), enc, "hi did not encrypt to BI via affine cipher")
        self.assertEqual(cipher_tools.apply_inverse_affine_cipher(enc,a,b), unenc,
        "BI did not convert back to hi via inverse affine cipher")

test = Test()
test.test_affine()