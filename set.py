s = {10,20,30,40,10,50}#it doesnt allow duplicate elements and omits them
print(s,type(s))
#set doesnt support indexing , repetition , slicing etc.
s.update([55,66])#it adds the elements to set but it adds randomly
print(s)
s.remove(50)
print(s)
#s.clear() - clears the set
print(len(s))#prints length of set
print(max(s))
s1 = frozenset(s)# converts to frozen set - it doesnt even supprot update or remove function
print(max(s1))
