m = (int)(input("Enter maths marks : "))
p = (int)(input("Enter physics marks : "))
c = (int)(input("Enter chemistry marks : "))

if m < 35 or p < 35 or c < 35 :
    print("You have failed in the examination")
else :
    avg = (m+p+c)/3
    if avg <= 59 : print("You have secured C grade")
    elif avg > 59 and avg <= 69 : print("You have secured B grade")
    elif avg > 69 : print("You have secured A grade")