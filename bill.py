u = (float)(input("Enter units consumed : "))
b = 0
if u <= 50 :
    b+= 0.5*u
elif u <= 150 :
    b+=25+0.75*(b-100)
elif u <= 250 :
    b+=100+1.25*(b-150)
elif u > 250 :
    b+=1.50*u

b+=0.17*b
print("Bill = Rs. ",b)