import requests

def testMonsterManual(base):
  print("Testing Monster Manual Table - ")
  print("Testing get - ")
  response = requests.get(base + "enemy/1", {})
  print(response.request, response.status_code)
  print(response.json(), "\n")
  
  print("Testing put - ")
  response = requests.put(base + "enemy/5", {"name":"buttmunch", "health":10, "armorClass":20, "movement":30, "size":"smol", "spellSlots":2})
  print(response.request, response.status_code)
  print(response.json(), "\n")

  print("Testing patch - ")
  response = requests.patch(base + "enemy/5", {"name":"buttmunch", "health":15, "armorClass":20, "movement":30, "size":"smol"})
  print(response.request, response.status_code)
  print(response.json(), "\n")
  
  print("Testing delete for non-existent enemy - ")
  response = requests.delete(base + "enemy/6")
  print(response.request, response.status_code)
  print(response.json(), "\n")

  print("Testing delete for existing enemy - ")
  response = requests.delete(base + "enemy/5")
  print(response.request, response.status_code)
  print(response.json(), "\n")
  