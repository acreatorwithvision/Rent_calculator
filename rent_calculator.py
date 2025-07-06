#Inputs needed
#Total rent, food ordered, groceries spent, total people living in room electricity spent and units per electricity.

#Output
#total amount you have to pay.

rent=int(input("Enter the amount of rent: "))
food=int(input("Enter the amount of food: "))
groceries=int(input("Enter the amount of groceries bought: "))
total_people=int(input("Enter the number of people staying: "))
electricity=int(input("electricity bill: "))
water_bill=int(input(water bill: ))
units=int(input("Enter the amount per unit: "))

total_bill=electricity * units
output=(rent+food+groceries+water_bill+total_bill)//total_people

print("Total amount you should pay is: ",output)
