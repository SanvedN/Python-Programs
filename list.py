list = [10 , 20 , 9.5 , "sanved", -1 , -99.3]
print(len(list))#displays the no of elements in list
print(list[1:3])#slicing : stores and prints the elements between the index numbers
print(list*2)#repetition : repeats list for number of times i.e. 2 times
print(list[5])#prints element in list at 5th index no position
list.append(40)#adds element at last of list
print(list)
list.remove('sanved')#removes the element from list
print (list)
del(list[0])
"""in-built function also used to delete element from list but it
removes elemnt according to index no and not value"""
print(list)
#list.clear() clears all elements from the list
#print(list)
print(max(list))#prints maximum/greatest value in the list
print(min(list))#prints minimum/smallest value in the list
#to print maximum or minimun value among list the elements are numerical here

l = ['a','ZB','Bac']
print(max(l))
print(min(l))
#max and min values for string are decided according to the length(no of characters in the string

list.insert(3,100)#inserts at 3rd index no the value 100
print(list)
list.sort()#this sorts list in ascending order and prints
print(list)
list.sort(reverse=True)#this sorts list in descending order
print(list)

l.sort(reverse=True)
"""sorting in strings is done based on alphabetical order prefrence
 is given to string starting with capital letters i.e. it is first in ascending order & last in descending"""
print(l)
print(l.index('a'))