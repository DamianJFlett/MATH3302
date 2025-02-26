import cipher_tools as ct
import unittest
class Test(unittest.TestCase):
    def test_affine(self):
        unenc = "hi"
        enc = "BI"
        aff = ct.Affine_Cipher(7,4)
        self.assertEqual(aff.encrypt(unenc), enc, "hi did not encrypt to BI via affine cipher")
        self.assertEqual(aff.decrypt(enc), unenc, "BI did not convert back to hi via inverse affine cipher")

test = Test()
test.test_affine()