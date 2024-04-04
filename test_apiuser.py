# test_api.py
import requests

API_URL = 'http://localhost:3000/users'  # Remplacez localhost:3000 par l'URL réelle de votre API

def test_get_users():
    response = requests.get(API_URL)
    assert response.status_code == 200
    users = response.json()
    for user in users:
        assert 'id' in user
        assert 'name' in user
        assert 'email' in user
