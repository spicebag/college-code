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
    cards = []
    loops = 5
    
    # Generates random number and assigns value.
number = randint(1, 13)
suitnumb = randint(1, 4)
suit = 0
    
    # Generates random number and assigns value.
number = randint(1, 13)
num = number
suitnumb = randint(1, 4)
suit = 0

   # Sets the suit.
if suitnumb == 1:
    suit = "Hearts"
elif suitnumb == 2:
    suit = "Clubs"
elif suitnumb == 3:
    suit = "Spades"
else:
    suit = "Diamonds"

   # Sets the number of the card.
    if number == 1:
        number = "Ace"
    elif number == 11:
        number = "Jack"
    elif number == 12:
        number = "Queen"
    elif number == 13:
        number = "King"
    else:
        number = str(number)

print("Generating card...")
time.sleep(0.5)
print("Generating card..")
time.sleep(0.5)
print("Generating card.")
time.sleep(0.5)
print ("*****")
card = (str(number)+ " of " +suit)
print(card)
print("*****")
choice = (input("Would you like to pick another card? (Y/N) "))
choice = choice.lower()



if choice == "Y":
        cards.append(card)
        loops = (loops - 1)
        
elif choice == "N":
        cards.append
