#-----------------------------------------------------------------------------
# Name:        Python 2 Assignment Re-Subbs (main.py)
# Purpose:     Show knowledge of new concpets learnt.
#
# Author:      Vinesh Vivekanand
# Created:     18-Jan-2021
# Updated:     01-Feb-2021
#-----------------------------------------------------------------------------

#Line (54 & 111): Introducing the function parameter 
#Line (56,57 & 72,73): Specifying the parameter that is invalid.


import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.info("Beginning of Program")
def medicine(animal):
  '''
  Calculates the amount of medication needed for each animal.

  Based on the animal inputted, this function will tell you the amount of medication needed for that animal as based on weight and other factors, the amount will vary.   

  Parameters
  ----------
  animal: strings
    The name of the different animals requiring medication.

  Returns
  -------
  float
    Returns a message based on the inputted animal. 

  Raises
  ------
  TypeError
    Raised if the animal parameter inputted is an incorrect type.
  ValueError
    Raised if user input is not in the animal species list.
  ''' 
  logging.info('The parameter inputted for the function is ' + str(animal))
  if not isinstance(animal,str):
	  logging.error( str(animal) + ' is not the correct type.')
	  raise TypeError( str(animal) + ' is not the correct type.')

  logging.debug('Everything has gone well, start to formulate medication amount')
  animalSpeciesList = ['dog', 'cat', 'lizard', 'bird', 'hamster', 'gerbil', 'snake', 'frog', 'geico', 'horse']
  #This is a set list of animals that must correspond with the user's inputs to continue with the program. 
  if animal in animalSpeciesList:
    #Various if and elif statements below are used to specify the different amount od medication for each animal inputted. 
    logging.info(str(animal) + ' is in the animal species list!')
    if animal == 'dog' or animal == 'cat':
      return ('A ' + str(animal) + ' would need 10g of medication')
    elif animal == 'lizard' or animal == 'bird' or animal == 'hamster' or animal == 'gerbil' or animal == 'snake' or animal == 'frog' or animal == 'geico':
      return('A ' + str(animal) + ' would need 5g of medication')
    elif animal == 'horse':
      return ('A ' + str(animal) + ' would need 15g of medication')
  else:
    logging.error(str(animal) + ' is an invalid value!')
    raise ValueError(str(animal) + ' is an invalid value!')
    #If the input is not in the list, it will then trigger the ValueError and print the message.   
    print('')


def payment(dog,cat,bird,lizard,gerbil,lost):
  '''
  Calculates the payment needed for customers.

  Veterinarians have to fix animal legs and each leg takes 15 min to heal. Each hour they are paid $20 for their services. This function calculates the total amount of money the customer has to pay the veterinarian office for their leg healing services. 

  Parameters
  ----------
  dog: int
    The number of dogs admitted into the office.
  cat: int
    The number of cats admitted into the office.
  bird: int
    The number of birds admitted into the office.
  lizard: int
    The number of lizards admitted into the office.
  gerbil: int
    The number of gerbils admitted into the office.
  lost: int
    The total number of legs lost by the animals.
  
  Returns
  -------
  float
    Total cost of the veterinarian's work.

  Raises
  ------
  TypeError
    Raised if any of the parameters are incorrect type.
  ValueError
    Raised if the parameters are negative and have an invalid value.
  ''' 
  logging.info('User inputted ' + str(dog) + ' dogs, ' + str(cat) + ' cats, ' + str(bird) + ' birds, ' + str(lizard) + ' lizards, and ' + str(gerbil) + ' gerbils. User also stated that there are ' + str(lost) + ' legs.')
  if not isinstance(dog,int) or not isinstance(cat,int) or not isinstance(bird, int) or not isinstance(lizard, int) or not isinstance(gerbil, int) or not isinstance(lost, int):
	  logging.error('One of the parameters is not the correct type.')
	  raise TypeError('One of the parameters is not the correct type.')
    #Checking if parameters are the valid types and making sure that value inputted is indeed an integer
  if dog < 0 or cat < 0 or bird < 0 or lizard < 0 or gerbil < 0 or lost < 0:
    logging.error('One of the parameters is an invalid value!')
    raise ValueError('One of the parameters is an invalid value!')
    #Makes sure that the values are not negative as if they are, the error message will print. 
  else: 
    logging.debug('Everything has gone well, start to calculate cost')
    totalLegs= (4 * dog) + (4 * cat) + (4 * lizard) + (4 * gerbil) + (2 * bird)
    hoursTaken= 0.25 * (totalLegs - lost)
    totalCost= hoursTaken * 20
    #Uses the amount of legs per animal, total time taken and cost per hour to calculate the total cost that the customer needs to pay.  
    if dog >= 3 and cat >= 3 and lizard >= 3 and gerbil >= 3 and bird >= 3: 
      finalCost = 0.80*totalCost
      #20% discount if a customer comes with more than 3 animals per species. 
      logging.debug('The 20% discount has been calculated. The final cost is ' + str(finalCost))
      return finalCost 
    else: 
      logging.debug('The customer had less than 3 animals per species, therefore had no 20% discount.  The final cost is ' + str(totalCost))
      return totalCost

# Testing function 1 (medicine function)
assert medicine('dog') == ('A dog would need 10g of medication'), "If dog is inputted, the printed message should say that a dog would need 10g of medication"
assert medicine('cat') == ('A cat would need 10g of medication'), "If cat is inputted, the printed message should say that a dog would need 10g of medication"
assert medicine('lizard') == ('A lizard would need 5g of medication'), "If lizard is inputted, the printed message should say that a dog would need 5g of medication"
assert medicine('hamster') == ('A hamster would need 5g of medication'), "If hamster is inputted, the printed message should say that a dog would need 5g of medication"
assert medicine('gerbil') == ('A gerbil would need 5g of medication'), "If gerbil is inputted, the printed message should say that a dog would need 5g of medication"
assert medicine('snake') == ('A snake would need 5g of medication'), "If snake is inputted, the printed message should say that a dog would need 5g of medication"
assert medicine('horse') == ('A horse would need 15g of medication'), "If horse is inputted, the printed message should say that a dog would need 15g of medication"
assert medicine('frog') == ('A frog would need 5g of medication'), "If frog is inputted, the printed message should say that a dog would need 5g of medication"
#Several asserts to test the outputs for each possible input in the medicine function.

# Testing function 2 (payment function)
assert payment(1,1,1,1,1,1) == 85.0, "If you have 1 dog, 1 cat, 1 bird, 1 lizard, 1 gerbil and 1 leg lost among them, you would have to pay $85.0"
assert payment(2,2,2,2,2,2) == 170.0, "If you have 2 dog, 2 cat, 2 bird, 2 lizard, 2 gerbil and 2 leg lost among them, you would have to pay $170.0"
assert payment(2,1,2,1,2,2) == 130.0, "If you have 2 dog, 1 cat, 2 bird, 1 lizard, 2 gerbil and 2 leg lost among them, you would have to pay $135.0"
assert payment(7,9,8,6,5,5) == 476.0, "If you have 7 dog, 9 cat, 8 bird, 6 lizard, 5 gerbil and 5 leg lost among them, you would have to pay $476.0"
assert payment(5,3,5,4,8,5) == 340.0, "If you have 1 dog, 1 cat, 1 bird, 1 lizard, 1 gerbil and 1 leg lost among them, you would have to pay $85.0"
assert payment(3,3,3,3,3,3) == 204.0, "If you have 1 dog, 1 cat, 1 bird, 1 lizard, 1 gerbil and 1 leg lost among them, you would have to pay $85.0"
assert payment(5,3,6,6,6,6) == 344.0, "If you have 1 dog, 1 cat, 1 bird, 1 lizard, 1 gerbil and 1 leg lost among them, you would have to pay $85.0"
assert payment(5,6,8,8,8,8) == 464.0, "If you have 1 dog, 1 cat, 1 bird, 1 lizard, 1 gerbil and 1 leg lost among them, you would have to pay $85.0"
#Several asserts to test the outputs for each possible input in the payment function.

print("At the veterinarian's office, when customers provide the the name of an animal, the verterinarians are able to disclose the amount of pain medication needed after surgery as the amount is different for each animal.")
print('')

#Within this while loop, we have the medication function's main code.
count=1
while count <= 3:
  try: 
    logging.debug('About to gather input from user for medicine()')
    inputAnimal=str(input('What animal do you have that needs medication? '))
    logging.info("The user inputted an animal for medication details: " + str(inputAnimal))
    print('')
    medicine(inputAnimal)
    print(medicine(inputAnimal))
    print('')
    #try block gathers input and calls and prints the function's return variable. 
  except TypeError:
    logging.error('One of the parameters is not the correct type.')
    print('One of the parameters is not the correct type.')
    count-=1
    #prevents the red error code of the program and instead prints the incorrect type message
  except ValueError:
    logging.error('One of the parameters is not the correct value.')
    print('One of the parameters is not the correct value.')
    count-=1
    #prevents the red error code of the program and instead prints the incorrect value message
  else:
    #Once there is a gurantee that the inputted values have no errors, proceed will the second input question
    logging.info('Try block was successful' + str(inputAnimal) + ' was inputted by the user')
    inputMoreAnimal=str(input('Do you have another animal that needs medication? '))
    print('')
    if inputMoreAnimal == 'yes' or inputMoreAnimal == 'Yes': 
      logging.debug("User inputted " + (str(inputMoreAnimal)) + " meaning they have another animal. Proceed to beginning of the loop to re-ask the first question.")
      count-=1
      #If "yes" is inputted the while loop continues and starts from the top, asking about another animal
    elif inputMoreAnimal == 'no' or inputMoreAnimal == 'No': 
      logging.debug("User inputted " + (str(inputMoreAnimal)) + " meaning they don't have another animal. Proceed to leg service questions.")
      count+=150
      print('Thank you!')
      print('')
      #If "no" is inputted the while loop ends and 
    else: 
      print("It was a yes or no question. That input doesn't work. Try again!!")
      print('')
      count-=1
      #If the user inputs anything other than yes or no, an erro message will appear and they will have the oppurtunity to input another animal. 

print("At the veterinarian office, they have various leg treatment services that help to fix any leg injuries as well as strengthen an animal's legs. Please fill out the questions below: ")
print('')

#Within this while loop, we have the payment function's main code.
var=1
while var <= 3:
  try:
    logging.debug('About to gather input from the user for the payment() function.')
    print('How many:')
    totalDog=int(input('Dogs do you have? '))
    totalCat=int(input('Cats do you have? '))
    totalBird=int(input('Birds do you have? '))
    totalLizard=int(input('Lizards do you have? '))
    totalGerbil=int(input('Gerbils do you have? '))
    print('')
    totalLostLegs=int(input('How many legs have your animals lost in total (if any)? '))
    cost= payment(totalDog,totalCat,totalBird,totalLizard,totalGerbil,totalLostLegs)
    #try block gathers input for different species calls the function's return variable.
  except TypeError as e:
    logging.error('One of the parameters is not the correct type.')
    print(str(e))
    print('')
    var-=1
    #prevents the red error code of the program and instead prints the incorrect type message
  except ValueError:
    logging.error('One of the parameters is not the correct value.')
    print("One of the inputs could not be converted.")
    print('')
    var-=1
    #prevents the red error code of the program and instead prints the incorrect value message
  else:
    logging.info('Try block was successful.')
    print('')
    print('Thank you for the inputs!')
    print('For the services provided, you will have to pay $' + str(cost))
    logging.info('The customer will have a final bill of: ' + str(cost))
    #Prints the total cost the customer has to pay for the service
    if totalDog >= 3 and totalCat >= 3 and totalLizard >= 3 and totalGerbil >= 3 and totalBird >= 3: 
      print ('Since you have more than 3 animals per species, you get a 20% discount')  
      #Prints message for the 20% discount 
    var+=15

#This concludes the program.









