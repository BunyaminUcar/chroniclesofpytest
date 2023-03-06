import pytest
from calculator import *

def test_status_code(url):
    assert status_code(url) == 200
          
def test_data(url):
    assert len(data(url)) != 0
   
def test_users(url):
    assert "Michael" in convertdata(url)
    assert "Rachel" in convertdata(url)


def test_modular_complete(complete):
    assert complete == "you and me are happy."



