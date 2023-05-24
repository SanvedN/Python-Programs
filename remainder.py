import math
def using_simple_operators(x,y) :
    q = (x/y)
    return abs(x-q)
def using_divmod(x,y) :
    return divmod(x,y)[1]
def using_mod_operator(x,y) :
    return x%y

if __name__ == "__main__" :
    x,y = [int(x) for x in input("Enter two numbers : ").split()]
    print("Remainder using +,-,*,/ operators : ",using_simple_operators(x,y))
    print("Remainder using divmod function : ",using_divmod(x,y))
    print("Remainder using % operator is ",using_mod_operator(x,y))