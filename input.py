s = input("Enter a string value:")#the message is displayed before inputing a value
#by default the value entered is string value
print(s , type(s))
#type casting is used to convert string data thats inputed to any type of data
i = (int)(input("Enter a number"))#this converts string type data to integer type
print(i)

#input multiple values by storing in a collection(list)
list = [int(x) for x in input("enter 3 numbers ").split()]#stores value in a list int(x) converts the variables in list to int
print(list)
#.split(seperator , limit) is used to seperate values by the specified seperator and limit