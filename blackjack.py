#
#
#
#

from random import randint
import time

# Get the users name and age and save it.
playeronename = input("What is your name? ")
playeroneage = int(input("What is your age? "))
playertwoname = input("What is your name? ")
playertwoage = int(input("What is your age? "))

# Print the users age
time.sleep(1)
print("-----------------------------------")
print("Player #1s name is", playeronename)
print(str(playeronename) + ", the age you have entered is " + str(playeroneage))
print(" ")
print("Player #2s name is", playertwoname)
print(str(playertwoname) + ", the age you have entered is " + str(playertwoage))
print("-----------------------------------")

# If playeroneage and playertwoage is over 18, then allow them to continue, if they are under 18 
# close the program.
print(' ')
if playeroneage < 18 or playertwoage < 18:
    print("You are not old enough to continue, please come back when you are over 18!")
    time.sleep(1)
    print("Closing in 5...")
    time.sleep(1)
    print("Closing in 4...")
    time.sleep(1)
    print("Closing in 3...")
    time.sleep(1)
    print("Closing in 2...")
    time.sleep(1)
    print("Closing in 1...")
    time.sleep(1)
    print("Closing...")
    quit()
else:
    print("You are old enough to continue, welcome")
0
