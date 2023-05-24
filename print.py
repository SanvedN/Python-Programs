print()
print("sanved " *4)#repetition
print("sanved".index('s'))
print("sanved \n  is great") #escape sequence \n prints the next string on a new line
print("sanved \t is the best")#\t prints the string seperated by tab i.e. 4 spaces

print(10 , 20)#here the seperator between the values is space : ' '
print(10 , 20 , sep='........') #sep= "string" is used to seperate the values or strings by the string enetred in the sepeartor

name = "sanved"
marks = 99.8
print(name,marks)
print("Name :" , name , "Marks :" , marks)
print("Name %s Marks %.2f" %(name,marks))#%s is placeholder for string type data and %f is placeholder for float data
#placeholders keep a place for a type of data whose value is given at the last
#%i is placeholder for integer type data
#.2f means that only 2 numbers will be displayed after decimal point in floating value . Any number can be placed in place of 2
#if we write %.0f then the floating value is converted to int value
print("Name {0} , Marks {1} ".format(name,marks))#instead of %f and %s just {} can be used as placeholder we can also use index no in {} : eg {0} , {1}