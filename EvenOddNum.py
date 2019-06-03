#Ask the user for a number. Depending on whether the number is even or odd,
#print out an appropriate message to the user.


number = int(input("Type a number: "))

remainder = number%2


if remainder == 0 :
    print("The number is even")
else:
    print("The number is odd")



             
