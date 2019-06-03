#Create a program that asks the user for a number and then prints out
#a list of all the divisors of that number.

number = int(input("Type a number: "))

listRange = list(range(1, number + 1))

listDivisors = []

    
for element in listRange:
    if number % element == 0:
        listDivisors.append(element)

    

print(listDivisors)  
    


