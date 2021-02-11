#-----------------------------------------------------------------------------
# Name:        For and While Loops (main.py)
# Purpose:     To understand how loops work 
#
# Author:      Vinesh Vivekanand 
# Created:     30-Nov-2020
# Updated:     30-Nov-2020
#-----------------------------------------------------------------------------

# Comment out the line below when you're done with the lesson code.
import loops

def factorial(number):
	# Returns the factorial
	# Use a while loop!
  add = 1 
  factorialProduct = 1 
  while (add < number):
    add= add + 1 
    factorialProduct = factorialProduct * add
  if number == 1 or number < 0: 
    return ("Error.")
  return (factorialProduct) 

	
def adder(begin, end):
	# Adds all integers between the two (inclusive) and returns.
	# Use a for loop!
  sumOfNumbers = 0
  for increaser in range(begin, end+1, 1):
    sumOfNumbers =  increaser + sumOfNumbers 
  if begin > end:
    return ("Error.")
  return sumOfNumbers 
	


# Main code - for testing.
print(factorial(5))

print(adder(5, 10))
