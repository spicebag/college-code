#
#
#
#
#

# Imports
import random

#1 = Clubs, 2 = Spades, 3 = Hearts, 4 = Diamonds
number1=random.randint(1,4)
number2=random.randint(1,13)

# Start of if statement to determine suite.
if number1==1:
    suite="Clubs"
elif number1==2:
    print("Spades")
    suite="Spades"
elif number1==3:
    print("Hearts")
    suite="Hearts"
else:
    print("Diamonds")
    suite="Diamonds"
    
# End of If Statement

# Start of if statement for card value.
if number2==11:
    print("Jack")
    card="Jack"
elif number2==12:
    print("Queen")
    card="Queen"
elif number2==13:
    print("King")
    card="King"
elif number2==1:
    print("Ace")
    card="Ace"
else:
    print(number2)

# Store the information
card=str(number2) + " of " + suite
print("Your card is the " + card + " of " + suite)