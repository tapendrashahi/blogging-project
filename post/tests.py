from django.test import TestCase
import requests

BASE_URL = "http://127.0.0.1:8000"

# Step 1: Get token
response = requests.post(f"{BASE_URL}/api/token/", json={
    "email": "info.tapendra@gmail.com",
    "password": "admin"
})

tokens = response.json()
access_token = tokens["access"]
print("Token:", access_token)

# Step 2: Use token to access protected endpoint
headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(f"{BASE_URL}/api/categories/", headers=headers)
print("Response text:", response.text) 
print("Categories:", response.json())
