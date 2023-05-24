#without returning value
def avg(a,b): #def used to define function
    avg = (a+b)/2
    print("Average =",avg)

a,b = [int(x) for x in input("Enter two numbers : ").split()]
avg(a,b) #invoking a function

#returning a value to main program
def avr(x,y):
    return (x+y)/2
x,y = [int(i) for i in input("Enter two numbers : ").split()]
print("Average =",avr(x,y))