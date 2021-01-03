import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "enemy/1", {})
print(response.json())
input()
response = requests.delete(BASE + "enemy/5")
print(response)