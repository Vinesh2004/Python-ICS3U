#-----------------------------------------------------------------------------
# Name: Lesson 1 - Basics (main.py)
# Purpose:  Test inputs and outputs 
#
# Author:      Vinesh Vivekanand 
# Created:     25-Nov-2020
# Updated:     25-Nov-2020
#-----------------------------------------------------------------------------

# This line will run the basics.py file (my example).
# You can comment this out when starting your exercise.
# All of your assignments/exercises should be written in main.py - you won't have to worry about this.
#import basics

# Start writing your code here!

#Scenario 1 
#input amount of apples and calculate the amount of apples they will eat if they save one apple
# Subtracted one from number inputed 
userInputApples= int(input('How many apples do I have?: \n'))
newAmountOfApples= userInputApples - 1
print("Because I am so hungry I will eat " + str(newAmountOfApples) + " apples!!")

print(" ")

#Scenario 2 
#Input any number and integer divides it by 2 
# States any remainders if the number inputed has any 
userInputNumber= int(input('Type a number: \n'))
calculationDivision= userInputNumber // 2
calculationRemainder= userInputNumber % 2
print("If you take the number " + str(userInputNumber) + " and divide it by 2, you will get " + str(calculationDivision) + " with a remainder of " + str(calculationRemainder))
 
print(" ")

#Scenario 3 
#Input three different integers and multiply the first two together 
#Take the product and root it to the third integer inputed 
userInputIntegerOne= int(input('Input a integer: '))
userInputIntegerTwo= int(input('Input another integer: '))
userInputIntegerThree= int(input('Input one more integer: '))
productOfOneAndTwo= userInputIntegerOne * userInputIntegerTwo 
exponentOfProduct= productOfOneAndTwo ** userInputIntegerThree 
print("By multiplying " + str(userInputIntegerOne) + " and " + str(userInputIntegerTwo) + " you get a product of " + str(productOfOneAndTwo))
print("If such product is then rooted to the power of " + str(userInputIntegerThree) + " the answer would then be " + str(exponentOfProduct))

print(" ")

#Scenario 4 
#Type a phrase of what the parrot might say 
#Input the amount of times you want it repeated 
userInputText= input("A parrot heard you say what phrase?: \n")
userInputRepetition = int(input("How many times should the parrot repeat what you said?: \n"))
outputSaid= userInputText * userInputRepetition
print('''The parrot yelled "''' + str( outputSaid) + '''" ''')

print(" ")

#Scenario 5 
#Input name and age and a random amount of days
#Calculate the age in years after that amount of days
userInputName= input("What is your name?: ") 
userInputAge= int(input("How old are you?: "))
userInputDays= int(input("State any amount of days: "))
changeInAge= userInputDays / 365
finalAge= changeInAge + userInputAge
print("In " + str(userInputDays) + " days " + userInputName + " will be " + str(finalAge) + " years old!")


print("\033[5;37;40m \033[0;37;40m\n")
print("HAVE A GREAT DAY " + userInputName + "!")
