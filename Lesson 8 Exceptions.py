#-----------------------------------------------------------------------------
# Name:        Exceptions (exceptions.py)
# Purpose:     Learning how to use Try/Except/Raise
#
# Author:      Vinesh Vivekanand
# Created:     06-Jan-2021
# Updated:     08-Jan-2021
#-----------------------------------------------------------------------------

#import example
#import exceptions

# Make a copy of your previous exercise and make modifications as per TASK.md
def simpleInterest(principal, rate, years):
	# Calculates the amount of simple interest earned on an initial investment
  if not isinstance(principal,(int,float)) or not isinstance(rate,int) or not isinstance(years, int):
    raise TypeError('One of the parameters is not the correct type.')
  if principal <= 0 or rate <= 0 or years <= 0:
	  raise ValueError('One of the parameters is an invalid value!')
  else:
	  interest = principal * (rate/100) * years
	  return interest

# Write some main code that makes multiple uses of this function.
# Try practicing previous skills such as: if statements, loops and lists!

#Asks for input for each student in the list 
#compares and returns largest interest made out of the students

print('In business class, students work with principals, rate and time period to understand how interest is calculated.')
print('')
interestList = []
studentList = ['Alvin', 'Billy', 'Chris', 'David', 'Eric']
var = 0
sorter=0
while var >= 0 and var < 5:
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
  try: 
    principalCalc2= int(input('Principal: '))
    rateCalc2= int(input('Rate: '))
    yearsCalc2= int(input('# of Years: '))
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
  try:
    principalCalc3= int(input('Principal: '))
    rateCalc3= int(input('Rate: '))
    yearsCalc3= int(input('# of Years: '))
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
