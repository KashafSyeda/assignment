print("Program compute the area")
r = int(input("enter radius"))
a = 3.14*r 
print(a)

print("program to check if a number is positive, negative or zero")
n = int(input("enter a number"))
if n == 0:
    print("number is zero")
elif n > 0:
    print("number is positive")
elif n < 0:
    print("number is negetive")    
else:
    print ("error")

print("check whether a number is completely divisible by another number") 
n1 = int(input("enter first number"))
n2 = int(input("enter second number"))
n = n1 % n2
if n == 0:
    print(str(n1) + " is divisible by " + str(n2))
else: print(str(n1) + " is not divisible by " + str(n2))    

print("program that computes the value of (n+nn+nnn)")
n = int(input("enter a number"))
o = n+n*n+n*n*n
print(o)