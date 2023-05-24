import math #this is math module . Modules are python scripts already built . This module already has the pi value

#finding the pi value by ourself
r = (float)(input("Enter radius of circle : "))
pi = 22/7
area = pi*r**2
print("Area of circle is : " , area)

#using math module
r2 = (float)(input("Enter radius of circle : "))
p = math.pi # here the value is calculated i.e. 3.14......
area = p*r2**2
print(area , p)