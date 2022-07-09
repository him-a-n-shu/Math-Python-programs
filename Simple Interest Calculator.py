heading="Simple Interest Calculator"
print(heading)

p = int(input("Enter Principle Amount: "))
r = int(input("Enter Rate of Interest: "))
t = int (input ("Enter Time Period: "))

sum = p*r*t/100

TA = p + sum

print ("Simple Interest: ", sum)
print("Total Amount To be Paid: ", TA)
