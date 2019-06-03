#Implement a function that takes as input three variables,
#and returns the largest of the three. Do this without using
#the Python max() function!

a = int(input("Type the first number: "))
b = int(input("Type the second number: "))
c = int(input("Type the thrid number: "))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
