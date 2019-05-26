print("Python program to convert height (in feet and inches) to centimetres")
#foot into cm multiply the length value by 30.48
#inch into cm multiply the length value by 2.54
h = float(input("enter height: "))
unit = str(input("press f for feet into cm \t or press i for inches into cm "))
if unit == 'f':
    height = h * 30.48
    print(str(height) + "cm")
elif unit == 'i': 
    height = h * 2.54
    print(str(height) + "cm")
else:
    print("error")    