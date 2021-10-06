#!python3
"""
A population can be modeled by the following:
future population = (current population)*(1+r)^(time in years) 
Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
Calculate the expected future population

Enter the population: 25000000
Enter the rate of growth in percent: 2.1
Enter the number of days: 12
There will be 25017087 people after 12 days
"""
import math

population = float(input("Enter the current population: "))
growth = float(input("Enter the rate of growth: "))
time = int(input("Enter the time in days: "))
fp = (population)*(1 + (growth / 100))**(time/365)
fp = round(fp)
print(f"There will be {fp} people after {time} days.")