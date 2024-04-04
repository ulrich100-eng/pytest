# test_api.py
import pytest
import requests

API_URL = 'http://localhost:3000'

def test_hello_world():
    response = requests.get(f'{API_URL}/hello')
    assert response.status_code == 200
    assert response.text == 'Helloworld'
