#hard-coded arrays name, pin and balance
balance=[450,930,192]
name=["Nova","Killian","Jonas"]
pin=[201,931,595]

#get the user to enter in their name and pin
search_name=input("Enter in your name")
search_pin=int(input("Enter in your pin"))

#check for correct login and get the user index
if search_name in name:
  index=name.index(search_name)
else:
  print("Name/Pin incorrect")
if pin[index]==search_pin:
  print("Succesfull login")
else:
   print ("Name/Pin incorrect")

#deposit money and print new balance
#get deposit amount amd add to current balance

print ("your balance is "+ str(balance[index]))
deposit_amount=int(input("Enter in your deposit amount"))
balance[index]=balance[index]+deposit_amount
print (balance[index])

print ("your balance is "+ str(balance[index]))
withdraw_amount=int(input("How much would you like to withdraw"))
balance[index]=balance[index]-withdraw_amount
print (balance[index])
