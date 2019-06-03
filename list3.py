#Take a list, say for example this one:

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#Ask the user for a number and return a list
#that contains only elements from the original list a
#that are smaller than that number given by the user.


a = [1,1,2,3,5,8,13,21,34,55,89]

b = []

number = int(input("Type a number: "))

for element in a:
    if element < number:
        b.append(element)

print(b)
        
