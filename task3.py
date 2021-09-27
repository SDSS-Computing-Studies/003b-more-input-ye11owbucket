#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""
p1 = float(input("Enter the first price: "))
p2 = float(input("Enter the second price: "))
p3 = float(input("Enter the third price: "))
p4 = float(input("Enter the fourth price: "))
p5 = float(input("Enter the fifth price: "))
sb = p1 + p2 + p3 + p4 + p5
tt = sb * .12
ft = sb + tt
sb2 = str(round(sb, 2))
tt2 = str(round(tt, 2))
ft2 = str(round(ft, 2))

sb3 = ("$" + str(sb2))
tt3 = ("$" + str(tt2))
ft3 = ("$" + str(ft2))

print("Your subtotal is" ,sb3, "and your taxes total" ,tt3, "for a total of" ,ft3,)


