import pytest
import requests

@pytest.fixture
def url():
    """Url geri döndürür"""
    return "https://reqres.in/api/users?page=2"


def data(url):
    r=requests.get(url)
    veri=r.json()
    data=veri["data"]
    return data

def convertdata(url):
    s=data(url)
    liste=[]
    for i in s: 
        liste.append(i['first_name'])
    return liste
    


def status_code(url1):
    r=requests.get(url1)
    return r.status_code




@pytest.fixture
def me():
    """Adımı yazdır"""
    return "me"


@pytest.fixture
def happy():
    """Mutlu yazdır"""
    return " are happy."


@pytest.fixture
def together(me):
    """adımızı yazdır"""
    return "you and " + me



@pytest.fixture
def complete(together, happy):
    """Birleştirir"""
    return together + happy




