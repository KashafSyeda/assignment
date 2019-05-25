First = int(input("enter first number "))
arithmetic_sign = str(input("Please enter '+','-','/','*',"))
Second = int(input("enter Second number"))
if arithmetic_sign == "+":
   print(First + Second)
elif arithmetic_sign == "-":
   print(First - Second)
elif arithmetic_sign == "*":
   print(First * Second)
elif arithmetic_sign == "/":
   print(First / Second)
else:
   print("check again")