import requests
import json

def testMonsterManual(base):
  print("Testing Monster Manual Table - ")
  print("Testing get - Should be 200 -")
  response = requests.get(base + "enemy/1", {})
  print(response.request, response.status_code)
  print(response.json(), "\n")
  
  print("Testing put - Should be 200 -")
  payload = {"name":"buttmunch", "health":10, "armorClass":20, "movement":30, "size":"smol", "spellSlots":2}
  response = requests.put(base + "enemy/5", json=payload)
  print(response.request, response.status_code)
  print(response.json(), "\n")

  print("Testing patch - Should be 200 -")
  payload = {"name":"buttmunch", "health":15, "armorClass":20, "movement":30, "size":"smol"}
  response = requests.patch(base + "enemy/5", json=payload)
  print(response.request, response.status_code)
  print(response.json(), "\n")
  
  print("Testing delete for non-existent enemy - Should be 404 - ")
  response = requests.delete(base + "enemy/6")
  print(response.request, response.status_code)
  print(response.json(), "\n")

  print("Testing delete for existing enemy - Should be 200 - ")
  response = requests.delete(base + "enemy/5")
  print(response.request, response.status_code)
  print(response.json(), "\n")
  