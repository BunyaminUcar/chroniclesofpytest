def  alan(r):
    return int(3.14 * r * r)

def test_alan():
    assert alan(3) == 28
    
def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test failed"
	assert x == y,"test failed"
def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed" 

import pytest

@pytest.fixture
def supply_AA_BB_CC():
	aa=25
	bb =35
	cc=45
	return [aa,bb,cc]

def test_comparewithAA(supply_AA_BB_CC):
	zz=35
	assert supply_AA_BB_CC[0]==zz,"aa and zz comparison failed"

def test_comparewithBB(supply_AA_BB_CC):
	zz=35
	assert supply_AA_BB_CC[1]==zz,"bb and zz comparison failed"

def test_comparewithCC(supply_AA_BB_CC):
	zz=35
	assert supply_AA_BB_CC[2]==zz,"cc and zz comparison failed"

@pytest.fixture
def supply_url():
	return "https://reqres.in"

import pytest
import requests
import json

def test_login_valid(supply_url):
	url = supply_url + "/login/" 
	data = {'email':'test@test.com','password':'something'}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 200, resp.text
	assert j['token'] == "QpwL5tke4Pnpja7X", resp.text

def test_login_no_password(supply_url):
	url = supply_url + "/login/" 
	data = {'email':'test@test.com'}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.text
	assert j['error'] == "Missing password", resp.text

def test_login_no_email(supply_url):
	url = supply_url + "/login/" 
	data = {}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.text
	assert j['error'] == "Missing email or username", resp.text