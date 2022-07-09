def SumN(n):
    sum1 = 0
    for i in range(1, n+1):
        sum1 += i
    print("The sum of first", n, "natural numbers is: ", sum1)

num = int(input("Enter value for n: "))
SumN(num)
