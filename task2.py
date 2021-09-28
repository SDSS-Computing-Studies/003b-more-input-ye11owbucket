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

pop = float(input('Enter the population: '))
rate = float(input('Enter the rate of growth in percent: '))
r = (rate / 100)
days0 = float(input('Enter the number of days: '))
days1 = days0 / 100
fp = (pop*(1+r)^int(days1 / 365))
days2 = str(days1)

print("There will be:", fp , "after", days2 ,"days")