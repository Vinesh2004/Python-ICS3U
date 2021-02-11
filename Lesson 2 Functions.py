#-----------------------------------------------------------------------------
# Name:        Functions
# Purpose:     Practice functions
#
# Author:      Vinesh Vivekanand
# Created:     14-Aug-2018
# Updated:     14-Aug-2018
#-----------------------------------------------------------------------------

# Lesson
import functions

def addNumbers(firstNum, secondNum):
	# Add the two given numbers and returns result

	# 'pass' is a placeholder if we have an empty function (or if statement/loop) - delete this when you start editing.
  additionOfNumbers = firstNum + secondNum
  return additionOfNumbers


# You write the next function!

def greeting(name):
  printMessage = '''Hello ''' + (str(name)) + ', nice to meet you!'
  return printMessage   

print(greeting('Rob'))
print(greeting('Bob'))
print(greeting('Dob'))
print(greeting('Fob')	)

print("The sum is: " + str(addNumbers(789,5456)))


# Main Code - for testing


#print(greeting('Mr. Kowalczewski'))
	
