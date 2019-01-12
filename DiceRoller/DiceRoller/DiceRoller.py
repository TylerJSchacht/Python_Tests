#-----------------------------------------------------------------------------------------------------------------
#
# Dice Roller
# By Tyler J. Schacht
# Date: January 10th, 2019
#
#-----------------------------------------------------------------------------------------------------------------

import random
import os

#-----------------------------------------------------------------------------------------------------------------
# --- Defining Functions -----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

# Will roll a number of dice with variable amount of sides.  If the user rolls more than one die, the total will also be calculated
def dice(sides=2, number=1):
	strSides = str(sides)
	print("Rolling d" + strSides + "(s)!")
	calcTotal = False
	if number > 1:
		calcTotal = True
	total=0
	while number >= 1:
		rolled = random.randint(1,sides)
		strRolled = str(rolled)
		print("You rolled a " + strRolled + "!")
		total = total + rolled
		number = number - 1
	if calcTotal:
		strTotal = str(total)
		print("You rolled in total " + strTotal + "!")

# Stops the user from putting in an answer that will break the program,  asks the user to reinput until they put in a number
def checkInt(userInput):
	if userInput.isnumeric():
		return int(userInput)
	else:
		while userInput.isnumeric() == False:
			print("I'm sorry please input a number:")
			userInput = input()
		return int(userInput)

# Stops the user from puting in an answer that is too low of a number for the dice roller to function.  Also uses the checkInt() function
def checkAmount(userInput, errorMsg, amountNeeded):
	while userInput < amountNeeded:
		print("Sorry, you need to " + errorMsg + ":")
		userInput = input()
		userInput = checkInt(userInput)
	return userInput

# I like to keep the command line clean :)
clear = lambda: os.system('cls')

#-----------------------------------------------------------------------------------------------------------------
#--- Main Function -----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

print("Please input the number of sides on the die/dice you want to roll (minimum of 2):")
input_sides = input()
input_sides = checkInt(input_sides)
input_sides = checkAmount(input_sides, "have at least 2 sides", 2)
clear()

print("Please input the number of dice you would like to roll (minimum of 1):")
input_number = input()
input_number = checkInt(input_number)
input_number = checkAmount(input_number, "roll at least one die", 1)
clear()

dice(input_sides, input_number)

#-----------------------------------------------------------------------------------------------------------------
#--- END ---------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------