#Let’s say I give you a list saved in a variable:
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].

#write code takes this list a and makes a new list that has
#only the even elements of this list in it.


a = [1,4,9,16,25,36,49,64,81,100]
b = []

for num in a:
    if num%2 == 0:
        b.append(num)

print(b)
        
        
