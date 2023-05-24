r = lambda a,b : a+b
#here lambda has multiple parmeters seperated by ','
a,b = [int(x) for x in input("Enter two numbers : ").split()]
print(r(a,b))