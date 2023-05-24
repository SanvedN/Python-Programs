import sys #imports sys module in program which contains the command line arguments
lst = sys.argv
print(lst)#the path of script is stored as default command line argument
print(len(lst))#length is 1 as the path is stored
#printing using loop
for i in lst : print(i)

print(sys.argv[0]) #or print(lst[0])
# #prints the path of the script as its the first command line arguments stored by default
