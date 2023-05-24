lst = [int(x) for x in input("Enter elements of the list : ").split()]
a = filter(lambda x : x%2==0 , lst )#assign filter function to  a variable
print(a , type(a))#it returns filter object and memory location of that object. It is necessary to convert it.
b = list(a)
print(b,type(b))