#-----------------------------------------------------------------------------
# Name:        Assertions (main.py)
# Purpose:     Testing code and functions
#
# Author:      Vinesh Vivekanand
# Created:     11-Jan-2021
# Updated:     13-Jan-2021
#-----------------------------------------------------------------------------

#import documentation

# Don't worry about making use of this function
# But add documentation and comments to it!

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
  if not isinstance(distance,(float,int)):
    # if the input is not a float or a int, then it will trigger a TypeError and print a message
    raise TypeError("Distance must be float or int.")
  if distance < 0:
    # if the input is negative it weill trigger a ValueError and print a different message
    raise ValueError("Distance must be greater than 0.")
  else:
    # if the input has no errors then follow this code
      km = round(distance * 1.60934,2)
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
    raise TypeError('One of the parameters is not the correct type.')
  if principal <= 0 or rate <= 0 or years <= 0:
    #makes sure it is not negative or an error message will be printed
	  raise ValueError('One of the parameters is an invalid value!')
  else:
	  interest = principal * (rate/100) * years
    #calculates the interest 
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
    principalCalc= int(input('What is the principal for ' + str(studentList[var]) + "'s investments?: "))
    rateCalc= int(input("What is the rate?: "))
    yearsCalc= int(input('For how many years is interest being gained?: '))
    interestCalculation = simpleInterest(principalCalc, rateCalc, yearsCalc)
    interestList.append(interestCalculation)
  except ValueError:
    print("One of the inputs could not be converted.")
    sorter+=1
  except TypeError as e:
    print(str(e))
    sorter+=1
  else:
    print("The interest " + str(studentList[var]) + " earned is: $" + str(interestCalculation))
  var+=1
  print(' ')
  
if sorter==0:
#Sorts the list of the interest only if all the students inputed proper values.
  interestList.sort()
  print('The largest amount of interest made of all the students is: $' + str(interestList[-1]))
  print(' ')
else:
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
    principalCalc2= int(input('Principal: '))
    rateCalc2= int(input('Rate: '))
    yearsCalc2= int(input('# of Years: '))
    #calculates the interest with the paramters inputed above
    interestCalculation2 = simpleInterest(principalCalc2, rateCalc2, yearsCalc2)
    print('The interest you made was: ' + str(interestCalculation2))
    if interestCalculation2 > comparingInterest:
      print('Congrats! That is correct!')
      count+=4
      print('')
    else: 
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
    principalCalc3= int(input('Principal: '))
    rateCalc3= int(input('Rate: '))
    yearsCalc3= int(input('# of Years: '))
    #calculates the interest with the paramters inputed above
    interestCalculation3 = simpleInterest(principalCalc3, rateCalc3, yearsCalc3)
    print('The interest you made was: ' + str(interestCalculation3))
    if interestCalculation3 < comparingInterest2:
      print('Congrats! That is correct!')
      count2+=4
      print('')
    else: 
      print('That is unfortunately incorrect, Try Again.')
      count2-=1
      print('')
  except ValueError:
    print("One of the inputs could not be converted.")
  except TypeError as e:
	  print(str(e))
