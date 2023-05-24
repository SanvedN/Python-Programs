a = (int)(input("Enter the starting number : "))
b =  (int)(input("Enter the ending number : "))
print("Odd numbers between" , a , "and" , b ,"are")
while a<= b :
    if a%2 != 0 : print(a)
    a += 1