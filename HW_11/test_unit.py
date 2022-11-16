import unittest
from signers import Signer


s = Signer(secret="aa", salt="bb")


class test_singer(unittest.TestCase):
    def test_1(self):
        self.assertEqual(type(s), Signer)

    def test_2(self):  # перевіряємо чи закодоване і потім розкодоване значення вірні
        data = {"name": "taras"}
        e_val = s.jwt_encode(data)
        d_val = s.jwt_decode(e_val)
        self.assertEqual(s.jwt_decode(e_val), {"name": "taras"})
        self.assertEqual(s.jwt_encode(d_val), e_val)

    def test_3(self):  # перевірєємо чи дійсно змінюються дані
        data = {"": ""}
        e_val = s.jwt_encode(data)
        d_val = s.jwt_decode(e_val)
        self.assertNotEqual(e_val, d_val)

    def test_4(self):  # перевіряємо чи дійсно отримуємо TypeError при неправильній подачі даних
        self.assertRaises(TypeError, Signer(1, 2))
        self.assertRaises(TypeError, Signer(0.5, 0.7))
        self.assertRaises(TypeError,Signer([1,], [1,]))
        self.assertRaises(TypeError, Signer((1,), (1,)))
        self.assertRaises(TypeError,Signer({1,},{1,}))
