#Write a program (function!) that takes a list and returns a new list
#that contains all the elements of the first list minus all the duplicates.


list1 = [1,5,86,12,4,7,36,12,2,1]
print(list1)
list2 =[]

def removeDuplicates (list2):
    for element in list1:
        list2.append(element)
        if list2.count(element) > 1:
            list2.remove(element)
            return list2

print (removeDuplicates(list2))


        
