a = 100 # integer type
b = 25.9 # floating point
c = 50.0
print(a,b,c)
print(type(a))
print(type(b))
print(type(c))

d = 3+5j # complex type
print(d)
print(type(d))

e = 0b1010 # binary value , '0b' shows its binary and converts it to decimal
print(e)# the value is converted from binary to decimal value

f = 0xff # ff is hexadecimal value , '0x' converts it to decimal value
print(f) # decimal value is printed

g = 0o10 # octadecimal value , 0o converts it to decimal
print(g)#decimal value printed

h = True #boolean type only carries true and false its called bool
print(h , type(h))
print(10<0)

#type conversion
i = 5.5
print(i , type(i))
j = int(i) #converts float to int
print(j , type(j))

k = bin(10)#converts decimal no to binary no
l = hex(10)#converts decimal no to hexadecimal no
m = oct(10)#onverts decimal no to octadecimal no
print (k , l ,m)

