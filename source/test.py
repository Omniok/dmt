import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "enemy/1", {})
input()
response = requests.delete(BASE + "enemy/4", {})
input()

print(response.json())