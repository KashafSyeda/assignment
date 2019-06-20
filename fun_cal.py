'''-----------Basic calculation through User defined function---------'''

a = int(input("enter number 1: "))
b = int(input("enter number 2: "))

def add(num1 , num2):
    my_sum = num1 + num2
    print(my_sum) 
add(a,b) 

def subtract(num1 , num2):
    subtract = num1 - num2
    print(subtract) 
subtract(a,b)  

def multiply(num1 , num2):
    multiply = num1 * num2
    print(multiply) 
multiply(a,b)  

def divide(num1 , num2):
    divide = num1/num2
    print(divide) 
divide(a,b) 

    