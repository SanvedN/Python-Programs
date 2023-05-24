x = int(input('Enter a number to check prime or not : '))
checkprime = True
if x == 1 :
    print("It is 1 . It is neither prime nor composite number")
    exit(0) #Control exits from program
elif x == 0 :
    print("The number is 0 . It is neither prime nor composite no")
    exit(0)#Control exits from program
else :
    for i in range(2,x):
        if x%i == 0: checkprime = False
if checkprime:
    print("Prime no")
else :
    print("Not prime no")