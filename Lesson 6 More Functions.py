#-----------------------------------------------------------------------------
# Name:        Functions2 (main.py)
# Purpose:     Create main code for a function e
#
# Author:      Vinesh Vivekanand 
# Created:     07-Dec-2020
# Updated:     07-Dec-2020
#-----------------------------------------------------------------------------

# Comment this out
#import functions
#import functions2

# You write the function yourself!

def milesToKm(distance):
  mileFactor = 1.60934
  if distance < 0: 
    return 'Error: negative distance.'
  else: 
    newDistance = distance * mileFactor
    kmDistance = round(newDistance,2)
    return kmDistance  


# Remove the comments when you're ready to test, but don't change the code!

assert milesToKm(10) == 16.09, "10 miles should be 16.09 km.  You returned: " + str(milesToKm(10))

assert milesToKm(18) == 28.97, "18 miles should be 28.97 km.  You returned: " + str(milesToKm(18))

assert milesToKm(-5) == 'Error: negative distance.', "-5 miles should return: 'Error: negative distance.'  You returned: " + str(milesToKm(-5))


# Write your own main code here that makes multiple uses of the function milesToKm() - similar to what I did for slopeCalc().  Be creative!

distanceRanMameer= int(input('How far did Mameer run in miles?:\n'))
mameerDistance= (milesToKm(distanceRanMameer))
zalikDistance= int(input('How far did Zalik run in km?:\n'))
print('Who ran a larger distance, Mameer or Zalik??')
print (" ")
if mameerDistance == 'Error: negative distance.':
  print ('Mameer has an invalid distance, therefore Zalik ran a larger distance')
else: 
  if mameerDistance > zalikDistance:
    print ("Mameer ran " + str(distanceRanMameer) + " miles, which when converted to Km is " + str(mameerDistance) + ". Therfore since Mameer's distance was larger than Zalik's, which was " + str(zalikDistance) + " Km, Mameer ran the larger distance!")
  elif mameerDistance == zalikDistance: 
    print ("They both ran " + str(zalikDistance) + " km!")
  else: 
    print ("Mameer ran " + str(distanceRanMameer) + " miles, which when converted to Km is " + str(mameerDistance) + ". Therfore since Mameer's distance was smaller than Zalik's, which was " + str(zalikDistance) + " Km, Zalik ran the larger distance!")


print(" ")
print(" ")
print("John Cena wanted to make clones of himself to see which one could run the farthest distance.")
print(" ")
clone1Dis= int(input('How far did clone 1 run in miles?: '))
clone2Dis= int(input('How far did clone 2 run in miles?: '))
clone3Dis= int(input('How far did clone 3 run in miles?: '))
clone4Dis= int(input('How far did clone 4 run in miles?: '))
johnClone1 = milesToKm(clone1Dis)
johnClone2 = milesToKm(clone2Dis)
johnClone3 = milesToKm(clone3Dis)
johnClone4 = milesToKm(clone4Dis)
print(" ")

if johnClone1 == 'Error: negative distance.':
  print ('There is an invalid distance')

else:
  totalDistance = johnClone1 + johnClone2 + johnClone3 + johnClone4 
  print("John Cena decided to enter the clones into a relay race, and they were able to run a toal of " + str(totalDistance) + " km before getting tired!")
  print(" ")

  print("John Cena needs the clones to run a total distance of 200km to get a world record. He needs to figure out the amount of miles the fourth clone shoudld run.")
  print(" ")
  undefinedDistance = 200 - johnClone1 - johnClone2 - johnClone3
  if undefinedDistance <= 0:
    print("Clone 4 is not needed as the other 3 can run the distance without the fourth")
  else: 
    mileFactor = 1.60934
    newClone4= undefinedDistance/mileFactor  
    finalClone4 = round(newClone4,2)
    print("After calculations, the fourth clone will need to run a distance of " + str(finalClone4) + " miles!")

