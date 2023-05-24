from functools import reduce #imports the function reduce from fucntools module , rather than importing whole module , only a particular function is imported
lst = [int(x) for x in input("Enter numbers of list : ").split()]
r = reduce(lambda x,y : x+y , lst)
print(r , type(r))#here an integer value is printed which is the sum of the list , it doesnt have any special reduce object valu or memory location of reduce object