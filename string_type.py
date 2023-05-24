s = 'My name is Sanved'
print(s)
s1 = '''Sanved Narwadkar
Valay Society
Hingne Mala
Sasane Nagar'''
print(s1)

i = s[0]#Stores the character present at index number 0 of string
print(i)

s2 = "Sanved"
print(s2*2)#Repetiton it repeats the string for fixed number of times

print(len(s2))#calculates length of string starting from 1

#slicing : removing some characters
print(s[0:3])
print(s[:5])
print(s[5:])
print("sanved" [3 : : -1])
print("sanved"[::-1])#reverses string
print("sanved".isspace())
x = "  I am great  "
print(x.strip())# strip() function removes all the spaces left before and after the string
print(x.lstrip())#removes left side spaces but keeps right side spaces
print(x.rstrip())#removes right side spaces
print(x.find("gr"))
print(x.count('a',5,11))#finds the number of times a string has occured in a string
print(x.upper())
print(x.lower())
print(x.title())