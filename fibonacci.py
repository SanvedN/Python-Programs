n = int(input("Enter number of terms of fibonacci series : "))
a = 0 ; b = 1
print(a , b , end= ' ')
i = 1
while i <= n-2 :
    c = a+b
    print(c,end=' ')
    a = b
    b = c
    i+=1