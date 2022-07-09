heading = "Welcome to Compound Interest calculator"

print(heading)

p = int(input ("Enter Principle Amount: "))
r = int(input ("Enter Rate of Interest: "))

t = int(input ("Enter Time of Interest: "))

sum = p*((1+r/100)**t)

print ("Compound Interest: ", sum)
