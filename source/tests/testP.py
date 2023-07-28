import requests
import json

def testPlayer(base):
  print("Testing Players Table - ")
  print("Testing get - Should be 200 -")
  response = requests.get(base + "player/1", {})
  print(response.request, response.status_code)
  print(response.json(), "\n")

  print("Testing put - Should be 200 -")
  payload = {"name":"Babe", "health":12, "armorClass":11, "movement":30, "size":"Medium", "spellSlots":2}
  response = requests.put(base + "player/2", json=payload)
  print(response.request, response.status_code)
  print(response.json(), "\n")

  print("Testing patch - Should be 200 -")
  payload = {"name":"Jerm", "health":15, "armorClass":14}
  response = requests.patch(base + "player/2", json=payload)
  print(response.request, response.status_code)
  print(response.json(), "\n")

  print("Testing delete for non-existent player - Should be 404 - ")
  response = requests.delete(base + "player/6")
  print(response.request, response.status_code)
  print(response.json(), "\n")

  print("Testing delete for existing player - Should be 200 - ")
  response = requests.delete(base + "player/2")
  print(response.request, response.status_code)
  print(response.json(), "\n")
