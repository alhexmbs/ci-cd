from main import Calculador

def test_sums_2_numbers():
    calc = Calculador()
    assert calc.sum(1, 2) == 3