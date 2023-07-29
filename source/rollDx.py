import random
import string

# Function to check if user input string is a dice roll
def is_dice_roll(rollText: str) -> bool:
  return rollText.startswith("/roll")

# Function to get the intended dice roll from user input string
def get_intended_dice_roll(rollText: str) -> list:
  rollText = rollText[5:] # Strip off "roll"
  rolls = rollText.split(" ")
  rolls = [i for i in rolls if i != ""] # Remove any empty strings
  # If the 1st element in the list is a number, then it's the number of dice to roll
  if rolls[0].isdigit():
    nDice = int(rolls[0])
    diceType = rolls[1]
  # Otherwise, the number of dice to roll is either not specified, or it's prepended to the dice type
  else:
    tempRollCheck = rolls[0].split("d") #Split any prepended number of dice from the dice type
    tempRollCheck = [i for i in tempRollCheck if i!= ""] # Remove any empty strings
    # If length of the list is 2, then there was a prepended number of dice
    if len(tempRollCheck) == 2:
      nDice = int(tempRollCheck[0])
      diceType = "d" + tempRollCheck[1]
    # Otherwise, there was no prepended number of dice
    else:
      nDice = 1
      diceType = rolls[0]
  
  return [nDice, diceType]

# Function to roll the dice and return a list of the rolls
def roll_dice(nDice: int, diceType: str) -> list[int]:
  diceRolls = []
  while nDice > 0:
    diceRoll = [] 
    if diceType == "d100":
      diceRoll = random.randint(1, 100)
    elif diceType == "d20":
      diceRoll = random.randint(1, 20)
    elif diceType == "d12":
      diceRoll = random.randint(1, 12)
    elif diceType == "d10":
      diceRoll = random.randint(1, 10)
    elif diceType == "d8":
      diceRoll = random.randint(1, 8)
    elif diceType == "d6":
      diceRoll = random.randint(1, 6)
    elif diceType == "d4":
      diceRoll = random.randint(1, 4)
    elif diceType == "d3":
      diceRoll = random.randint(1, 3)
    elif diceType == "d2":
      diceRoll = random.randint(1, 2)
    diceRolls.append(diceRoll)
    nDice -= 1
    
  return diceRolls