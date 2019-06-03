#Write a program that takes a list of numbers and makes a new list of only
#the first and last elements of the given list.
#For practice, write this code inside a function.


a = [42,5,69,7,3,1,0,8,15,37]

def edges (a):
    return (a[0], a[len(a)-1])

print(edges(a))
