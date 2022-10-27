#
#
# @(#)Loop2.py
# This program prints the square of the numbers 1 to 10
# @Killian
# @Version 1.0.0

# For loop to print numbers to screen
for x in range(1,11):
    print(x*x) 
    
#
# @(#)UserInput.py
# This demonstrates the use of a for loop
# @Killian
# @Version 1.0.0

# Prompt user for first number
num1=int(input("\nEnter in the first number:"))
total=num1
print("The total is: " +str(total))

num2=int(input("\nEnter in the second number:"))
total=num2
print("The total is: " +str(total))

num3=int(input("\nEnter in the third number:"))
total=num3
print("The total is: " +str(total))

# @(#)ForInput2.py
# This demonstrates the use of a for loop
# The program uses a for loop to get 5 numbers from the user.
# It displays the total and the average of these numbers
# @Killian
# @Version 1.0.0

# Initializse variables
total=0
average=0

# For loop to get numbers and calculate the total
for x in range(1,6):
    num=int(input("\nEnter a number: "+str(x) +";"))
    total=total +num
print("The total is: " +str(total))
print("\n The average is " +str(total/(x)))
