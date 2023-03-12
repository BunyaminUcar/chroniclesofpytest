import pytest

def cevre_hesapla(a,b):
    return (a+b)*2

@pytest.fixture()
def ucgen():
    print("Üçgen oluşturuldu")
    yield
    print("Üçgen silindi")

def test_ucgen_cevresi_hesaplama(ucgen):
    assert cevre_hesapla(3,4) == 14

def test_ucgen_alan_hesaplama(ucgen):
    assert cevre_hesapla(3,4) == 14
