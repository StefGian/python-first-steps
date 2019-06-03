name = input("Type your name: ")
age = int(input("Type your age: "))

#while age <0:
    #print("The age should be positive")
    #age = int(input("Type your age: ")
     
weight = float(input("Type your weight: "))


if age<=17:
    color = "white"
elif age<=24:
    color = "pink"
elif age<=35:
    color = "red"
elif age<=45:
    color = "green"
elif age<=55:
    color = "blue"
else:
    color = "black"


if weight < 50:
    size = "Small"
elif weight<=64:
    size = "Medium"
elif weight<=79:
    size = "Large"
else:
    size = "X-Large"


print ("Hey " + name + ",it is cool to be ", age, "years old!")
print ("You should buy a " + color + " " , size , " shirt.")
    
    
# second way

#Ta prwta idia
colors = ["white", "pink", "red", "green", "blue", "black"]
shirtSizes = ["Small", "Medium", "Large", "X-Large"]

userColor = ""
userShirtSize = ""

if age >= 0 and <= 17:
    userColor = colors[0]
elif age > 17 and age<=24:
    userColor = colors[1]
elif age > 24 and age <=35:
    userColor = colors[2]
elif age > 35 and age <=45:
    userColor = colors[3]
elif age > 45 and age <=55:
    userColor = colors[4]
else:
    userColor = colors[5]
          

if weight <=50:
    userShrtSize = shirtSizes[0]
elif weight>50 and weight <=640:
    userShrtSize = shirtSizes[1]
elif weight >64 and weight <=79:
    userShrtSize = shirtSizes[2]
else:
    userShirtSize = shirtSizes[3]

#ta print idia
    
