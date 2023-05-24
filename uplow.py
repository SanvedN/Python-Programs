def mtd1(c) :
    if c[0].isupper() :
        print("Character is upper case")
    elif c[0].islower() :
        print("Character is lower case")
    else :
        print("Not an alphabet")

def mtd2(c) :
    if ord(c[0]) in range(65,91) :
        print("Character is upper case")
    elif ord(c[0]) in range(97,123) :
        print("Character is lower case")
    else :
        print("Not an alphabet")

def mtd3(c) :
    if c[0] >= 'a' and c[0] <= 'z' :
        print("Character is lower case")
    elif c[0] >= 'A' and c[0] <= 'Z' :
        print("Character is upper case")
    else :
        print("Not an alphabet")
if __name__ == "__main__" :
    c = input("Enter a character : ")
    mtd1(c)
    mtd2(c)
    mtd3(c)