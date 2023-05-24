def res(a,b):
    return a+b,a-b,a*b,a/b,a%b #multiple values are returned using ',' but they are stored in a tuple

a,b = [int(x) for x in input("Enter two numbers : ").split()]
print("Results =")
for i in res(a,b):
    print(i)