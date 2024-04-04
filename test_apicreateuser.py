# test_create_users.py
import pytest
import requests

API_URL = 'http://localhost:3000/users'

def test_create_user():
    user_data = {"id": 1, "name": "John Doe", "email": "john@example.com"}
    response = requests.post(API_URL, json=user_data)
    assert response.status_code == 201
    assert response.json() == user_data
