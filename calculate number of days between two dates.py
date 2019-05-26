print("program to calculate number of days between two dates")
d1 = int(input("enter first date"))
d2 = int(input('enter sec date'))
if d1 > 31:
    print ("wrong entry")
elif d2 > 31:
    print ("wrong entry")
else:
    d = d2 - d1
print (d)