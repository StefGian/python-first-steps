#first method with or
age = input("How old are you?")
if(int(age)> 18 or int(age)<13) :
    print("you are not a teenager")
else:
    print("you are a teenager")



#second method with and
age = input("How old are you?")
if(int(age)< 18 and int(age)>=13) :
    print("you are a teenager")
else:
    print("you are not a teenager")


#third method using if
age = input("how old are you?")
age = int(age)
if age >=13:
    if age <=18:
        print("you are a teenager")
    else:
        print("you are not a teenager")
else:
    print("you are not a teenager")
