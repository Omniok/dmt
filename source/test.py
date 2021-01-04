import requests

BASE = "http://127.0.0.1:5000/"

print("Testing get - ")
response = requests.get(BASE + "enemy/1", {})
print(response.json())
input()
print("Testing put - ")
response = requests.put(BASE + "enemy/5", {"name":"buttmunch", "health":10, "armorClass":20, "movement":30, "size":"smol"})
print(response.json())
input()
print("Testing patch - ")
response = requests.patch(BASE + "enemy/5", {"name":"buttmunch", "health":15, "armorClass":20, "movement":30, "size":"smol"})
print(response.json())
input()
print("Testing delete - ")
response = requests.delete(BASE + "enemy/6")
print(response.json())
