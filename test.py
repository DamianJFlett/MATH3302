import cipher_tools as ct
import unittest
class Test(unittest.TestCase):
    def test_affine(self):
        unenc = "hi"
        enc = "BI"
        aff = ct.Affine_Cipher(7,4)
        self.assertEqual(aff.encrypt(unenc), enc, "hi did not encrypt to BI via affine cipher")
        self.assertEqual(aff.decrypt(enc), unenc, "BI did not convert back to hi via inverse affine cipher")

    def test_caesar(self):
        shif = ct.Caesar_Cipher(12)
        enc = "QGDAHUEUAZ"
        unenc = "eurovision"
        self.assertEqual(shif.decrypt(enc),  unenc, " shift cipher didn't decrypt correctly")
        self.assertEqual(shif.encrypt(unenc), enc, "shift cipher did not encrypt correctly")
    
    def test_hill(self):
        self.assertRaises(ValueError, ct.HillCipher.__init__, (ct.HillCipher(),[[1,3,3],[1,5,6],[5,6,4,7]]))
        self.assertRaises(ValueError, ct.HillCipher.__init__, (ct.HillCipher(),[[1,0,0],[0,0,0],[0,0,0]]))


test = Test()
test.test_affine()
test.test_caesar()
test.test_hill()