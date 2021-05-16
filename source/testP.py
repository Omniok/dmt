import requests

BASE = "http://127.0.0.1:5000/"

print("Testing Players Table - ")
print("Testing get - ")
response = requests.get(BASE + "player/1", {})
print(response.json())
input()
print("Testing put - ")
response = requests.put(BASE + "player/2", {"name":"Babe","health":"12", "armorClass":11, "movement":30, "size":"Medium", "spellSlots":2})
print(response.json())
print("Testing patch - ")
response = requests.patch(BASE + "player/2", {"name":"Jerm","health":"15", "armorClass":14})
print(response.json())
input()
print("Testing delete for non-existent player - ")
response = requests.delete(BASE + "player/6")
print(response.json())
input()
print("Testing delete for existing player - ")
response = requests.delete(BASE + "player/2")
print(response.json())
