#opening and reading the file
f = open('text.txt','r')
t = f.read()

#counting the number of 'the' in the file
i = 0
for s in t.lower().split() :
    if s == 'the' :
        i+=1
print("Number of 'the' in the file = ",i)

#to print number of words
print("Number of words = ",len(t.split()))

#to print number of lines
i=0
print("Number of lines = ",len(t.split('\n')))