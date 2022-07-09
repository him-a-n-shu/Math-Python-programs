#In this program, we will find the roots of Quadratic Equation.

import math
heading = "Welcome to Quadratic Roots Calculator\nThe Standard Form of Quadaric Equation is ax^2+bx+c.\nAccording to Standard Form, Give values of following: "
print (heading)

a = int (input ("Value of 'a': "))
b= int (input ("Value of 'b' : "))
c = int(input ("Value of 'c': "))
d = (b**2)-(4*a*c)

print ("The Discriminant of Equation is", d)


#Case 1
if d>0:
    print ("It has Real and Distinct Roots")

    rootl= (-b + math.sqrt(d)) / (2*a)
    print("Root 1 is", rootl)

    root2 = (-b - math.sqrt(d)) / (2*a)
    print ("Root 2 is", root2)


#Case 2
elif d==0:
    print ("It has Real and Equal Roots")
    rootl= (-b + math.sqrt(d)) / (2*a)
    print ("Root 1 is", rootl)

    root2= (-b - math.sqrt(d)) / (2*a)
    print ("Root 2 is", root2)


#Case 3
else:
    print ("It has no Real Roots")
    print ("Goodbye! \nHave a Nice Day.")
