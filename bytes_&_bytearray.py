list = [1,2,3,4,5,6,255]
print(list , type(list))

b = bytes(list)#converts list to byte - byte range from 0 - 256
print(b , type(b))
print(b*2)
print(b.index(6))
print(b[0:3])
b1 = bytearray(list)
print(b1,type(b1))
b1.remove((3))
print(b1)
print(b1*2)
print(b1.index(255))
print(b1[3:4])