limit = (int)(input("Enter the limit of numbers to enter : "))
lis = [(int)(x) for x in input("Enter numbers : ").split(" ",limit-1)]
prod = 1
for i in lis :
    prod *= i

print("Product = ",prod)