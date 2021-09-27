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
v = "$"
principal = float(input('Enter your amount: '))
rate = float(input('Enter the rate: '))
r = (rate / 100)
time = float(input('Enter the # of days: '))
x= (principal*r*time)/365
round(x, 2)
print("You earned:", v,x, "interest")

