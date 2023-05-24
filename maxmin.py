num = int(input("Enter amount of numbers : "))
li=[]
for i in range(0,num) :
    li.append(int(input("Enter element ")))
print("Max = ",max(li))
print("Min = ",min(li))
print("Sum = ",sum(li))
print("Average = ",(sum(li)/num))