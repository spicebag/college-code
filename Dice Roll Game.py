
#
#
#
import random
from random import randint

# Declare variables and generate a random number between 1 and 6.
dice = random.randint(1,6) # Call a randint from the random library.


# Start of if statement to determine if a user wins (Heads and Six)
if (dice==1 or dice ==3 or dice ==5):
        print("You threw a "+ str(dice) + ", You win!")
else:
    print("You threw a "+ str(dice) + ", You lose.")
# End of if statement.