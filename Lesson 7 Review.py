#-----------------------------------------------------------------------------
# Name:        Review of Lessons (main.py)
# Purpose:     To review the concepts previously learned 
#
# Author:      Vinesh Vivekanand 
# Created:     04-Jan-2020
# Updated:     04-Jan-2020
#-----------------------------------------------------------------------------

#import example

def simpleInterest(principal, rate, years):
	# Calculates the amount of simple interest earned on an initial investment

	if principal <= 0 or rate <= 0 or years <= 0:
		return "Error"
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
while var >= 0 and var < 5:
  principalCalc= int(input('What is the principal for ' + str(studentList[var]) + "'s investments?: "))
  rateCalc= int(input("What is the rate?: "))
  yearsCalc= int(input('For how many years is interest being gained?: '))
  interestCalculation = simpleInterest(principalCalc, rateCalc, yearsCalc)
  if interestCalculation == "Error":
	  print("Something went wrong! Try Again.")
  else:
	  print("The interest " + str(studentList[var]) + " earned is: $" + str(interestCalculation))
  interestList.append(interestCalculation)
  print(' ')
  var+=1

interestList.sort()
print('The largest amount of interest made of all the students is: $' + str(interestList[-1]))
print(' ')


#checks and compares your interest made to John Cena's
comparingInterest= (simpleInterest(1000,5,3)) 
print("The students are then asked to try and create values for principal, rate and years so the interest made is LARGER than that of John Cena's")
print("John Cena's Interest: " + str(comparingInterest))


count=3 
while count > 0 and count < 4:
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

#checks and compares your interest made to Jefferson's
comparingInterest2= (simpleInterest(10,50,10)) 
print("They are then asked to input values for principal, rate and years so the interest made is SMALLER than that of Jefferson's")
print("Jefferson's: " + str(comparingInterest2))


count2=3 
while count2 > 0 and count2 < 4:
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

    
