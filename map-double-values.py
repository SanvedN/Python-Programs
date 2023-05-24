lst = [int(x) for x in input("Enter elements of the list : ").split()]
r = map(lambda x : x*2 , lst)#map function doesnt check condition it performs calculation
print(r , type(r))#its printed as map object and the memory location of that object
a = list(r)
print(a,type(a))