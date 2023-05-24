#consider the following list and perfom the following operations
A = ['hello','sanved','22211539','python for engineers','viit pune','study hard']

#add your roll number at position 3
A[2] = '176'

#add python programming at the end
A.append('python programming')
print(A)
#add two more courses into the list
A.insert(4,'bxe')
A.insert(4,'smart sensors')
print(A)
#delete hello from the list
A.remove('hello')
print(A)
#delete study hard from the list
A.remove('study hard')
print(A)
#count python from the list
c=0
for i in A :
    if 'python' in i:
        c+=1
print(c)
#return substrings of the list
for i in A :
    print(i.split())
#return length of list
print(len(A))
#reverse list
A.reverse()
print(A)
#return empty list
A.clear()
print(A)