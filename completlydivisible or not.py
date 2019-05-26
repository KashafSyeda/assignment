print("check whether a number is completely divisible by another number") 
n1 = int(input("enter first number"))
n2 = int(input("enter second number"))
n = n1 % n2
if n == 0:
    print(str(n1) + " is divisible by " + str(n2))
else: print(str(n1) + " is not divisible by " + str(n2))  