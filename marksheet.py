print("Markseet")

a = int(input("Number in Chemistry  :   "))
b = int(input("Number in Sindhi     :   "))
c = int(input("Number in Urdu       :   "))
d = int(input("Number in Physics    :   "))
e = int(input("Number in Maths      :   "))
f = 100*(a+b+c+d+e)//500
print(f)
if f > 85 and f < 90:
    print("A Grade")
elif f < 80 and f > 75:
    print("B Grade")
elif f < 70 and f > 65:
    print("C Grade")
elif f < 50 :
    print("FAIL SORRY")    

else:
    print("Thank you for your supporting")