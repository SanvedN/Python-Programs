def fac(n):
    if n == 0 :
        res = 1
    else :
        res = n*fac(n-1)#here the function fac is calling itself within its body - recursion 
    return res
if __name__ == "__main__" :
    print(fac(n=int(input('enter number : '))))