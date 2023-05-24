#cube of number using a function
def cb(n):
    return n**3
a = int(input("Enter number to find cube : "))
print(cb(a))

#cube of number using lambda
f = lambda n : n**3  #lambda function assigned to a variable
n = int(input("Enter number to find cube : "))
print(f(n))#the variable to which lambda is assigned is invoked as a function with () and parameters 