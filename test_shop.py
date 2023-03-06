import pytest
from shop import ShoppingCart

def test_elemanekle():
    
    cart = ShoppingCart(5)
    
    cart.add("elma")
    
    assert cart.size() == 1
    
def test_eklenen_eleman_kontrolu():
    
    cart = ShoppingCart(5)
    
    cart.add("elma")
    
    assert "elma" in cart.get_items() 


def test_sepet_eleman_sayısı_kontrolu():
    
    cart = ShoppingCart(5)
    
    for _ in range(5):
        cart.add("elma")
    
    with pytest.raises(OverflowError):
        cart.add("elma")
    
def test_sepet_toplam_fiyat():
    
    cart = ShoppingCart(5)
    
    cart.add("elma")
    cart.add("armut")
    
    price_map = {"elma": 5, "armut": 10}
    
    assert cart.get_total_price(price_map) == 15
