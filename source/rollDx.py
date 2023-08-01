import random
import string

# Function to check if user input string is a dice roll
def is_dice_roll(rollText: str) -> bool:
  return rollText.startswith("/roll")

# Function to get the intended dice roll from user input string
def get_intended_dice_roll(rollText: str) -> list:
  rollText = rollText[5:] # Strip off "/roll"
  rolls = rollText.split(" ") # Tokenize roll text
  rolls = [i for i in rolls if i != ""] # Remove any empty strings 
  # If the 1st element in the list is a number, then it's the number of dice to roll
  # e.g., "/roll 2 d6"
  if rolls[0].isdigit():
    nDice = int(rolls[0])
    diceType = int(rolls[1].replace("d", "")) # Strip off "d" from the dice type
  # Otherwise, the number of dice to roll is either not specified, or it's prepended to the dice type
  # e.g., "/roll d100" or "/roll 2d6"
  else:
    # Check to see dice type and ensure is separate from number of rolls to be made
    rolls = rolls[0].split("d") #Split any prepended number of dice from the dice type
    rolls = [i for i in rolls if i != ""] # Remove any empty strings
    # If length of the list is 2, then there was a prepended number of dice
    # The "/roll 2d6" case
    if len(rolls) == 2:
      nDice = int(rolls[0])
      diceType = int(rolls[1])
    # Otherwise, there was no prepended number of dice
    # The "/roll d100" case
    else:
      nDice = 1
      diceType = int(rolls[0])
  
  return [nDice, diceType]

# Function to roll the dice and return a list of the rolls
def roll_dice(nDice: int, diceType: int) -> list[int]:
  diceRolls = [] # List of dice rolls
  # Roll given number of dice and dice type
  while nDice > 0: 
    # Roll a die of diceType and append to list of dice rolls
    diceRolls.append(random.randint(1, diceType)) 
    nDice -= 1 # Decrement the number of dice to roll
    
  return diceRolls