from HW_11.signers import Signer

s = Signer("aa", "bb")
data = {"name": "taras"}
s_e = s.jwt_encode(data)
s_d = s.jwt_decode(s_e)


def test_1():  # перевіряємо ідентичність до кодуванні і після
    assert s_d == data

def test_2():  # перевіряємо чи дійсно дані змінюються
    assert s_e != s_d
