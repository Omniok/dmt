import importlib
import os,sys
# Append current working directory to sys.path to enable import of rollDx
sys.path.append(os.getcwd())
importlib.import_module("rollDx", package="rollDx.py",)
from rollDx import *

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Test can verify if is dice roll
print("Checking if can recognize dice roll")
rollAttempt = "/roll d20"
print(is_dice_roll(rollAttempt))

print("Checking if can recognize non-dice roll")
nonRollAttempt = "booty d10"
print(is_dice_roll(nonRollAttempt))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# Test that can roll 1 die without specifying quantity explicitly
print("Checking if can roll a d20 without specifying quantity explicitly")
roll_d20 = "/roll d20"
diceRollIntent = get_intended_dice_roll(roll_d20)
print("Rolls - ")
print(roll_dice(diceRollIntent[0], diceRollIntent[1]))

print("Checking if can roll a d10 without specifying quantity explicitly")
roll_d10 = "/roll d10"
diceRollIntent = get_intended_dice_roll(roll_d10)
print("Rolls -")
print(roll_dice(diceRollIntent[0], diceRollIntent[1]))

# Test can roll die while explicitly defining quantity
print("Checking if can roll one d20 while specifying quantity explicitly")
rollOne_d20 = "/roll 1d20"
diceRollIntent = get_intended_dice_roll(rollOne_d20)
print("Rolls - ")
print(roll_dice(diceRollIntent[0], diceRollIntent[1]))

print("Checking if can roll four d10 while specifying quantity explicitly")
rollFour_d10 = "/roll 4d10"
diceRollIntent = get_intended_dice_roll(rollFour_d10)
print("Rolls - ")
print(roll_dice(diceRollIntent[0], diceRollIntent[1]))

# Test can roll die while specifying quantity with spaces between quanity and type
print("Checking if can roll one d20 while specifying quantity with spaces between quantity and type")
rollOne_d20 = "/roll 1 d20"
diceRollIntent = get_intended_dice_roll(rollOne_d20)
print("Rolls - ")
print(roll_dice(diceRollIntent[0], diceRollIntent[1]))

print("Checking if can roll four d10 while specifying quantity with spaces between quantity and type")
rollFour_d10 = "/roll 4  d10"
diceRollIntent = get_intended_dice_roll(rollFour_d10)
print("Rolls - ")
print(roll_dice(diceRollIntent[0], diceRollIntent[1]))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")