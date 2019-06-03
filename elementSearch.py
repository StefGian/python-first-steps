#Write a function that takes an ordered list of numbers
#(a list where the elements are in order from smallest to largest)
#and another number. The function decides whether or not the given number
#is inside the list and returns (then prints) an appropriate boolean.

list1 = [1,2,5,7,12,29,31,36,43,45,62,77,81,90]

number = 9

def search(list1):
    for element in list1:
        if number in list1:
            return True
        else:
            return False

print(search(list1))
