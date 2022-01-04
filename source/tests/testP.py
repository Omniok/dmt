import requests

def testPlayer(base):
  print("Testing Players Table - ")
  print("Testing get - ")
  response = requests.get(base + "player/1", {})
  print(response.request, response.status_code)
  print(response.json(), "\n")

  print("Testing put - ")
  response = requests.put(base + "player/2", {"name":"Babe","health":"12", "armorClass":11, "movement":30, "size":"Medium", "spellSlots":2})
  print(response.request, response.status_code)
  print(response.json(), "\n")

  print("Testing patch - ")
  response = requests.patch(base + "player/2", {"name":"Jerm","health":"15", "armorClass":14})
  print(response.request, response.status_code)
  print(response.json(), "\n")

  print("Testing delete for non-existent player - ")
  response = requests.delete(base + "player/6")
  print(response.request, response.status_code)
  print(response.json(), "\n")

  print("Testing delete for existing player - ")
  response = requests.delete(base + "player/2")
  print(response.request, response.status_code)
  print(response.json(), "\n")
