#-----------------------------------------------------------------------------
# Name:        Python Assignment 1 (main.py)
# Purpose:     Showcase knowledge of python concepts.
#
# Author:      Vinesh Vivekanand 
# Created:     10-Dec-2020 
# Updated:     18-Dec-2020
#----------------------------------------------------------------------------

#Function that calculates volume 
def rectangularPrismVolume(width,length,height):
  if width > 0 and length > 0 and height > 0 and width <= 50 and length <= 50 and height <= 50: 
    volume= width * length * height 
    roundedVolume=round(volume,0)
    return roundedVolume
  else: 
    print ("That does not work!")
    exit()

#Function that adds,removes items from lists at a certain index 
def changeList(colourListAnswer,inputChangeColour,index,colour):
  if inputChangeColour == 'add':
    coloursInList = ['black', 'pink', 'indigo', 'green', 'navy', 'white', 'purple', 'orange', 'grey', 'maroon', 'coral', 'brown', 'red', 'blue', 'yellow']
    if index >= -2 and colour in coloursInList:
      colourListAnswer.insert(index, colour)
      return colourListAnswer
    else:
      print('That does not work')
      exit()
  elif inputChangeColour == 'remove':
    if index >= -2:
      del colourListAnswer[index]
      colour=colour
      return colourListAnswer
    else:
      print('That does not work')
      exit()


#Explanation of Scenario
print('On your way to school, a CIA officer approaches you in hopes of recruiting you for their organization. They heard from your teachers that you were smart but they wanted to test you for themselves!')

#While loop that allows you to input weight and height to check if it meets paramters (repeats 3 times)
print(' ')
print('First, the CIA wants to make sure that you are human and not a robot!')
print('Answer the following questions!')
var = 3
while var > 0 and var < 4:
  print('')
  height= float(input('How tall are you(feet)?: \n'))
  weight= float(input('How much do you weigh(pounds)?: \n'))

  if (height > 4.5 and height < 6.5) and (weight > 70.0 and weight < 250.0):
    print("You passed the first test, you're definitely human!")
    var=var+4
  elif (height > 4.5 and height < 6.5) and (weight < 70.0 or weight > 250.0):
    print('You are suspicous of being a robot!')
    var=var+4
  elif (height < 4.5 or height > 6.5) and (weight > 70.0 and weight < 250.0):
    print('You are suspicous of being a robot!')
    var=var+4
  elif (height < 4.5 or height > 6.5) and (weight < 70.0 or weight > 250.0):
    print('Error: You are a robot. Retry. ' + str(var-1) + ' more attempts.')
    var=var-1

if var==0:
  exit()

#Checks the vowels in a list, then adds it to another list
if var>=4:
  print('')
  wordList= (input('Type a word/sentence/letters with vowels: \n'))
  characters= list(wordList)
  vowels=[]
  numbersInWord=0
  continuation=0

  for chars in characters:
    if chars in "0123456789":
      numbersInWord+=1
    elif chars in "aeiouyAEIOUY":
      vowels.append(chars)
  
  numberOfVowels= len(vowels)
  print(' ')

  if numbersInWord > 0:
    print("Why are there numbers?")
  elif numberOfVowels==0: 
    print('Error: No vowels')
  elif numberOfVowels >= 1:
    vowelAnswer = int(input("How many vowels are there in the word(s)/sentence/letters?: \n"))
    if numberOfVowels == vowelAnswer:
      print("You were correct congratulations!") 
      continuation+=1
    elif numberOfVowels != vowelAnswer:
      print('You were incorrect, Robot Detected')
      print('Correct Answer: ' + str(numberOfVowels))
      
else:
  print("You're a robot; You're Not Welcome")

#Acts as a boolean statement; causes the end of the code
if continuation == 0:
  print (" ")
  print("YOU HAVE FAILED THE CIA TEST!")
  exit()

print(' ')
print('Now its time to test your math knowledge! The CIA wants to see if you are truly intelligent!')

#First use of math function (finds difference)
print('Input Values for Rectangular Prism 1 (1-50)')
inputWidth1= int(input('Width: '))
inputLength1= int(input('Length: '))
inputHeight1= int(input('Height: '))
print (' ')

print('Input Values for Rectangular Prism 2 (1-50)')
inputWidth2= int(input('Width: '))
inputLength2= int(input('Length: '))
inputHeight2= int(input('Height: '))
print (' ')

#Calls the function
prismEndValue1 = (rectangularPrismVolume(inputWidth1,inputLength1,inputHeight1))
prismEndValue2 = (rectangularPrismVolume(inputWidth2,inputLength2,inputHeight2))

if prismEndValue1 >= prismEndValue2:
  prismDifference = int(prismEndValue1) - int(prismEndValue2)
  prismDifferenceAnswer= int(input('What is the difference between the volume of prism 1 and 2?: \n'))
  if prismDifference==prismDifferenceAnswer:
    print ('Correct! The difference is indeed: ' + str(prismDifference))
  else: 
    print ('Wrong! The difference was: ' + str(prismDifference))
    exit()
else: 
  prismDifference = int(prismEndValue2) - int(prismEndValue1)
  prismDifferenceAnswer= int(input('What is the difference between the volume of prism 2 and 1?: \n'))
  if prismDifference==prismDifferenceAnswer:
    print ('Correct! The difference is indeed: ' + str(prismDifference))
  else: 
    print ('Wrong! The difference was: ' + str(prismDifference))
    exit()

#Second use of math function (division of volume)
print (' ')
print('You have to choose the dimensions of 2 cubes, input the measurement for each cube:')
inputMeasurement1= int(input('Cube 1: '))
inputMeasurement2= int(input('Cube 2: '))

#Calls the function
cubeMeasurement1 = (rectangularPrismVolume(inputMeasurement1,inputMeasurement1,inputMeasurement1))
cubeMeasurement2 = (rectangularPrismVolume(inputMeasurement2,inputMeasurement2,inputMeasurement2))

if cubeMeasurement1 >= cubeMeasurement2:
  prismQuotient = int(cubeMeasurement1) / int(cubeMeasurement2)
  prismQuotientAnswer= int(input('How many cube 2s can fit into cube 1s?: \n'))
  if prismQuotient==prismQuotientAnswer:
    print ('Correct! The quotient is indeed: ' + str(prismQuotient))
  elif prismQuotientAnswer <= prismQuotient + 3 and prismQuotientAnswer >= prismQuotient - 3:
    print ('Close Enough, Good Job! The quotient was: ' + str(prismQuotient))
  else: 
    print ('Wrong! The quotient was: ' + str(prismQuotient))
else: 
  prismQuotient = int(cubeMeasurement2) / int(cubeMeasurement1)
  prismQuotientAnswer= int(input('How many cube 1s can fit into cube 2s?: \n'))
  if prismQuotient==prismQuotientAnswer:
    print ('Correct! The quotient is indeed: ' + str(prismQuotient))
  elif prismQuotientAnswer <= prismQuotient + 1 and prismQuotientAnswer >= prismQuotient - 1:
    print ('Close Enough, Good Job! The quotient was: ' + str(prismQuotient))
  else: 
    print ('Wrong! The quotient was: ' + str(prismQuotient))
    exit()
    
#Third use of math function (problem solving of volumes with multipliers)
print (' ')
prismVar= 5
while prismVar > 0 and prismVar < 6:
  print('You have a certain multiplier (8 and 1) that multiplies the volume of your prism. Create values for two prisms that when added,  fit within a 100 unit³ prism (you may have a remainder of 10)')
  print()
  print('')
  print('Prism 1: (multiplier of 8)')
  widthInput1= int(input('Width: '))
  lengthInput1= int(input('Length: '))
  heightInput1= int(input('Height: '))
  print('')
  print('Prism 2:(multiplier of 1)')
  widthInput2= int(input('Width: '))
  lengthInput2= int(input('Length: '))
  heightInput2= int(input('Height: '))

  #Calls the function  
  prismMeasurement1 = (rectangularPrismVolume(widthInput1,lengthInput1,heightInput1))
  prismMeasurement2 = (rectangularPrismVolume(widthInput2,lengthInput2,heightInput2))
    
  addPrism = (prismMeasurement1 * 8) + (prismMeasurement2 * 1)

  if (100-addPrism) <= 10 and (100-addPrism) >= 0 and prismMeasurement1 >= 0 and prismMeasurement2 >= 0:
    print('Correct!! Your total volume is ' + str(addPrism) + ' with a remainder of ' + str(100-addPrism) )
    prismVar+=7 
  else:
    print('RETRY: Incorrect :( Your multiplier gave the total volume of ' + str(addPrism) + ' You have ' + str(prismVar) + ' tries left' + '.\n')
    prismVar-=1

# Answer: 2x2x2 (8 multiply)
        #  3x2x6 (1 mulitply)
        # = 100


print ('')
highestNumber = int(input('Give any postive integer (larger the more difficult): \n '))
print ('')

#Checks what remainder the number has to determine if even or odd then add or subtract
highestNumberAnswer=0
for addSubtractNumber in range(1, highestNumber+1):
  if addSubtractNumber % 2 == 1:
    highestNumberAnswer += addSubtractNumber
  else:
      highestNumberAnswer -= addSubtractNumber   

highestNumberInput = int(input('If you subtract every even number and add every odd number within ' + str(highestNumber) + ' what is the total sum?: \n')) 
print ('')

#Gives different responses based on answer inputted
if highestNumber <=10:
  if highestNumberAnswer == highestNumberInput:
    print ("Good Job, that is correct!")
  else: 
    print('Sorry! That is incorrect! The correct answer was ' + str(highestNumberAnswer))
    exit()
elif highestNumber >=10 and highestNumber <=99:
  if highestNumberAnswer == highestNumberInput:
    print ("Excellent Job, that is correct and impressive!")
  else:
    print('Sorry! That is incorrect! The correct answer was ' + str(highestNumberAnswer))
    exit()
elif highestNumber >=100:
  if highestNumberAnswer == highestNumberInput:
    print ("That is amazing! Outstanding work!")
  else:
    print('Sorry! That is incorrect! The correct answer was ' + str(highestNumberAnswer))
    exit()

print(' ')
print('Now lets test your english knowledge and mental capacity!')
print('')
colourList = ['red', 'blue', 'yellow']
print('Currently in the list you have the colours: Red, Blue, Yellow')

print("Input colours to be alphabetically ordered")
print("Type 'passcode' when you are done adding colours")

possibleColourInputList = ['black', 'pink', 'green','brown', 'white','purple','orange','grey','maroon','passcode']

#Inputs different colours and ends additions when you type 'passcode'
print ('')
colourVar=10 
while colourVar>0: 
  colourInput= input('Input as many colours as you want!: ')
  if colourInput.lower() not in colourList and colourInput.lower() in possibleColourInputList:
    colourList.append(colourInput.lower())
  elif colourInput.lower() in colourList:
    print('That colour already exists!')
    continue
  else:
    print('That is not valid as a colour!')
    continue
  if colourInput== ('passcode'):
    if len(colourList) == 4:
      print('You tried to cheat!')
      exit()
    else:
      print('You have completed entering colours!')
      colourVar-=123   
  else: 
      colourVar-=1      
  
if 'passcode' in colourList:
  del colourList[-1]

print("")
print("In your list, you currently have:")

for i in range(0, len(colourList), 1):
  print(colourList[i])

#Allows you to input the order and checks with the already sorted list
print("")
print('List the colours in alphabetical order')
colourListAnswer = []
for count in range(0,len(colourList),1):
  colourInputAnswer= input('')
  colourListAnswer.append(colourInputAnswer)

colourList.sort()

#works to replace spacing after colour is typed
numCorrect = 0
for i in range(0,len(colourList)):
  colourList[i] = colourList[i].replace(" ", "")
  colourListAnswer[i] = colourListAnswer[i].replace(" ", "")
  if colourList[i] == colourListAnswer[i]:
    numCorrect += 1

if numCorrect == len(colourList):
  print(' ')
  print("Good Job! That was the right order!")
else: 
  print('This is the correct answer' + str(colourList))
  print('But this is what you wrote' + str(colourListAnswer))
  exit()

print(' ')
print('Choose to add or remove colours from the list above to match the list below\n', 'New List: \n')
comparingColourList= ['brown', 'black', 'blue', 'pink', 'red', 'purple']
comparingColourList.sort()

for colours in comparingColourList:
  print(colours)

oldList=len(colourListAnswer)

#Calls the function to add and remove colours from list previously made
colourVariable=1
changedColourList = []
numberOfAnswers = 0

while colourVariable > 0:
  print (' ')
  inputChangeColour=input('Type Add or Remove:  ')
  if inputChangeColour == 'add':
    colour=input('Input Colour to change:  ')
    index=int(input('Input index (starts at 0):  '))
    changedColourList=(changeList(colourListAnswer,inputChangeColour,index,colour))
    print(changedColourList)
    colourVariable+=1
    numberOfAnswers += 1
        
  elif inputChangeColour == 'remove':
    index=int(input('Input index (starts at 0):  '))
    colour='blank'
    changedColourList=(changeList(colourListAnswer,inputChangeColour,index,colour))
    print(changedColourList)
    colourVariable+=1
    numberOfAnswers += 1
  else: 
    print('\n That does not work')


  #verify the lists are correct  
  if numberOfAnswers > 0:
    if changedColourList[0] == comparingColourList[0] and changedColourList[1] == comparingColourList[1] and changedColourList[2] == comparingColourList[2] and changedColourList[3] == comparingColourList[3] and changedColourList[4] == comparingColourList[4] and changedColourList[5] == comparingColourList[5] and len(changedColourList) == len(comparingColourList):
      print(' ')
      print("Good Job! That was the right order!")
      print('')
      print('CONGRATS YOU PASSED. YOU ARE OFFICIALLY A CIA INTERN!')
      colourVariable-=20
    elif colourVariable == oldList + 3:
      print(' ')
      print("You took too long! You don't deserve to join the CIA")
      exit()
    
    numberOfAnswers = 0

    #Code ends

