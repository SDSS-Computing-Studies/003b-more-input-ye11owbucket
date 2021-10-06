#!python3
 
"""
##### Task 1
The bank calculates the amount of interest you earn using the simple interest formula:
interest = principal * rate * #days in the month / 365

Ask the user to enter the amount of their principal, the number of days in the month the 
rate of interest expressed as a percentage. 
 Calculate the amount of interest they would be paid.

example:
Enter your amount: 100
Enter the rate: 2.5
Enter the # of days in the month: 30
You earned $0.2 interest. 
(2 points) 
"""
import math

amount = float(input("Enter your amount: "))
rate = float(input("Enter your interest rate: "))
days = float(input("Enter days this month: "))
interest = (amount * rate * days / 365) / 100
temp1 = interest*100
temp1 = math.floor(temp1)
interest = temp1/100
interest = round(interest, 2)
print(f"You earned ${interest} interest.")

