#-----------------------------------------------------------------------------
# Name:        Logging (main.py)
# Purpose:     Making sure the code runs properly 
#
# Author:      Vinesh Vivekanand 
# Created:     13-Jan-2021
# Updated:     13-Jan-2021
#-----------------------------------------------------------------------------

import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.info("Beginning of Program")
def milesToKm(distance):
  '''
  Convert distance into km.

  Calculates the km by taking the distance in miles and multiplying it by 1.60934, which is the multiplyer to convert between the two measurements of distance.

  Parameters
  ----------
  distance: int/float
    The distance in miles.
  
  Returns
  -------
  float
    Distance in Km after the conversion.

  Raises
  ------
  TypeError
    Raised if any of the parameters are incorrect type.
  ValueError
    Raised if numMarks is greater than total, or if numMarks or total is negative.
  '''
  logging.info("milesToKm() function begins with distance of: " +str(distance))

  if not isinstance(distance,(float,int)):
    # if the input is not a float or a int, then it will trigger a TypeError and print a message
    logging.error('One of the parameters is not the correct type.')
    raise TypeError("Distance must be float or int.")
  if distance < 0:
    # if the input is negative it weill trigger a ValueError and print a different message
    logging.error('One of the parameters is an invalid value!')
    raise ValueError("Distance must be greater than 0.")
  else:
    # if the input has no errors then follow this code
      logging.debug('Everything has gone well, start to calculate Km')
      km = round(distance * 1.60934,2)
      logging.info('The calculation product is' + str(km))
      return km

# Copy your previous exercise, add documentation + comments

def simpleInterest(principal, rate, years):
  '''
	Calculates the simple interest.

	Calculates the interest by multiplying the principal by the years and multiplying the rate after it is divided by 100. Calculation is only done if parameters are acceptable (numbers > 0).

	Parameters
	----------
	principal : int
		The intial amount of money before interest.
	rate: int
		The interest rate.
	years : int
		The amount of years the principal is gaining interest.

	Returns
	-------
	float
		The calculated interest with the three parameters.

	Raises
	------
	TypeError
		Raised if any of the parameters are incorrect type.
	ValueError
		Raised if numMarks is greater than total, or if numMarks or total is negative.
	'''
	# Calculates the amount of simple interest earned on an initial investment
  if not isinstance(principal,(int)) or not isinstance(rate,int) or not isinstance(years, int):
    #checks the types of each parameter of the function 
    logging.error('One of the parameters is not the correct type.')
    raise TypeError('One of the parameters is not the correct type.')
  if principal <= 0 or rate <= 0 or years <= 0:
    #makes sure it is not negative or an error message will be printed
    logging.error('One of the parameters is an invalid value!')
    raise ValueError('One of the parameters is an invalid value!')
  else:
    logging.debug('Everything has gone well, start to calculate interest')
    interest = principal * (rate/100) * years
    #calculates the interest 
    logging.info('Interest is calculated to be: ' + str(interest))
    return interest

# Testing function 1
assert milesToKm(1) == 1.61, "1 mile should be 1.61km"
assert milesToKm(30) == 48.28, "30 miles should be 48.28km"
assert milesToKm(10) == 16.09, "10 miles should be 16.09km"
assert milesToKm(15.6) == 25.11, "15.9 miles should be 25.11km"
assert milesToKm(12.7) == 20.44, "12.7 miles should be 20.44km"


# Testing function 2
assert simpleInterest(10,32,5) == 16.0, "The interest should be 16.0"
assert simpleInterest(54,12,10) == 64.8, "The interest should be 64.8"
assert simpleInterest(45,65,2) == 58.5, "The interest should be 58.5"
assert simpleInterest(2,2,2) == 0.08, "The interest should be 0.08"
assert simpleInterest(5,6,5) == 1.5, "The interest should be 1.5"



#Asks for input for each student in the list 
#compares and returns largest interest made out of the students

print('In business class, students work with principals, rate and time period to understand how interest is calculated.')
print('')
interestList = []
studentList = ['Alvin', 'Billy', 'Chris', 'David', 'Eric']
var = 0
sorter=0
#Creates the lists and sets the variables used in the while loop
while var >= 0 and var < 5:
#repeats the while loop 5 times, enough to cycle through all the names in the list.  
  try:
    logging.debug('About to gather input from user')
    principalCalc= int(input('What is the principal for ' + str(studentList[var]) + "'s investments?: "))
    rateCalc= int(input("What is the rate?: "))
    yearsCalc= int(input('For how many years is interest being gained?: '))
    logging.info('User inputted ' + str(principalCalc) + ' for the principal, ' + str(rateCalc) + ' for the rate and ' + str(yearsCalc) + ' for the number of years')
    interestCalculation = simpleInterest(principalCalc, rateCalc, yearsCalc)
    interestList.append(interestCalculation)
  except ValueError:
    logging.error('One of the parameters is not the correct value.')
    print("One of the inputs could not be converted.")
    sorter+=1
  except TypeError as e:
    logging.error('One of the parameters is not the correct type.')
    print(str(e))
    sorter+=1
  else:
    logging.info('Try block was successful. ' + str(studentList[var]) + " earned is: $" + str(interestCalculation))
    print("The interest " + str(studentList[var]) + " earned is: $" + str(interestCalculation))
  var+=1
  print(' ')
  
if sorter==0:
#Sorts the list of the interest only if all the students inputed proper values.
  interestList.sort()
  print('The largest amount of interest made of all the students is: $' + str(interestList[-1]))
  print(' ')
else:
  logging.error('One or more of the parameters is not the correct value or type.')
  print('Not sufficient entries, cannot compare interests.')
  print(' ')


#checks and compares your interest made to John Cena's
comparingInterest= (simpleInterest(1000,5,3)) 
print("The students are then asked to try and create values for principal, rate and years so the interest made is LARGER than that of John Cena's")
print("John Cena's Interest: " + str(comparingInterest))


count=3 
while count > 0 and count < 4:
#repeats the process of creating interest that is larger than John Cena's three times
  try: 
    logging.debug('About to gather input from user')
    principalCalc2= int(input('Principal: '))
    rateCalc2= int(input('Rate: '))
    yearsCalc2= int(input('# of Years: '))
    logging.info('User inputted ' + str(principalCalc2) + ' for the principal, ' + str(rateCalc2) + ' for the rate and ' + str(yearsCalc2) + ' for the number of years.')
    #calculates the interest with the paramters inputed above
    interestCalculation2 = simpleInterest(principalCalc2, rateCalc2, yearsCalc2)
    print('The interest you made was: ' + str(interestCalculation2))
    if interestCalculation2 > comparingInterest:
      logging.info('That is correct. Your interest ($' + str(interestCalculation2) + ') is greater than John Cenas ($' + str(comparingInterest) + ').')
      print('Congrats! That is correct!')
      count+=4
      print('')
    else: 
      logging.error('Your input of ' + str(interestCalculation2) + ' is incorrect!')
      print('That is unfortunately incorrect, Try Again.')
      count-=1
      print('')
  except ValueError:
    print("One of the inputs could not be converted.")
  except TypeError as e:
	  print(str(e))

  

#checks and compares your interest made to Jefferson's
comparingInterest2= (simpleInterest(10,50,10)) 
print("They are then asked to input values for principal, rate and years so the interest made is SMALLER than that of Jefferson's")
print("Jefferson's: " + str(comparingInterest2))


count2=3 
while count2 > 0 and count2 < 4:
#repeats the process of creating interest that is smaller than Jefferson's three times
  try:
    logging.debug('About to gather input from user')
    principalCalc3= int(input('Principal: '))
    rateCalc3= int(input('Rate: '))
    yearsCalc3= int(input('# of Years: '))
    logging.info('User inputted ' + str(principalCalc3) + ' for the principal, ' + str(rateCalc3) + ' for the rate and ' + str(yearsCalc3) + ' for the number of years.')
    #calculates the interest with the paramters inputed above
    interestCalculation3 = simpleInterest(principalCalc3, rateCalc3, yearsCalc3)
    print('The interest you made was: ' + str(interestCalculation3))
    if interestCalculation3 < comparingInterest2:
      logging.info('That is correct. Your interest ($' + str(interestCalculation3) + ') is smaller than Jeffersons ($' + str(comparingInterest2) + ').')
      print('Congrats! That is correct!')
      count2+=4
      print('')
    else: 
      logging.error('Your input of ' + str(interestCalculation3) + ' is incorrect!')
      print('That is unfortunately incorrect, Try Again.')
      count2-=1
      print('')
  except ValueError:
    print("One of the inputs could not be converted.")
  except TypeError as e:
	  print(str(e))
