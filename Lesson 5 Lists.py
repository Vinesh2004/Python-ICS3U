#-----------------------------------------------------------------------------
# Name:        Lists (main.py)
# Purpose:     Maintain a grocery list 
#
# Author:      Vinesh Vivekanand
# Created:     02-Dec-2020
# Updated:     02-Dec-2020
#-----------------------------------------------------------------------------

# Lesson files
import lists

# Add 'item' to groceryList, sort and returns the list.
def addToList(groceryList, item):
  if item not in groceryList:
    groceryList.append(item)
    groceryList.sort()
    return groceryList
  else: 
     return ('Error.')
    
	# Remove 'item' and return groceryList.
def removeFromList(groceryList, item):
  if item not in groceryList:
    return ('Error.')
  else: 
    groceryList.remove(item)
    return groceryList 
	
	# Returns the first 'number' of items in groceryList
def returnItems(groceryList, number):
  if number > len(groceryList):
    return ('Error.')
  else: 
    grocery =  groceryList[0:number]
    return (grocery)
	
	
# Main code - for testing.  You don't have to change the list, but do try different values of add/removing/returning.


print(addToList(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 'bacon'))

print(removeFromList(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 'apples'))

print(returnItems(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 3))




# Remove the comments when you're ready to test, but don't change the code!

assert addToList(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 'bacon') == ['apples', 'bacon', 'chicken', 'eggs', 'ice cream', 'soup'], "Adding 'bacon' to the list ['chicken', 'apples', 'soup', 'ice cream', 'eggs'] should return: ['apples', 'bacon', 'chicken', 'eggs', 'ice cream', 'soup'].  You have returned: " + str(addToList(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 'bacon'))

assert addToList(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 'chicken') == "Error.", "Adding 'chicken' to the list ['chicken', 'apples', 'soup', 'ice cream', 'eggs'] should return: Error.  You have returned: " + str(addToList(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 'chicken'))

assert removeFromList(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 'apples') == ['chicken', 'soup', 'ice cream', 'eggs'], "Removing 'apples' from ['chicken', 'apples', 'soup', 'ice cream', 'eggs'] should return: ['chicken', 'soup', 'ice cream', 'eggs'].  You have returned: " + str(removeFromList(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 'apples'))

assert removeFromList(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 'coke') == "Error.", "Removing 'coke' from ['chicken', 'apples', 'soup', 'ice cream', 'eggs'] should return: Error.  You have returned: " + str(removeFromList(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 'coke'))

assert returnItems(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 3) == ['chicken', 'apples', 'soup'], "The first 3 items in ['chicken', 'apples', 'soup', 'ice cream', 'eggs'] should return: ['chicken', 'apples', 'soup'].  You have returned: " + str(returnItems(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 3))

assert returnItems(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 10) == "Error.", "The first 10 items in ['chicken', 'apples', 'soup', 'ice cream', 'eggs'] should return: Error.  You have returned: " + str(returnItems(['chicken', 'apples', 'soup', 'ice cream', 'eggs'], 10))



