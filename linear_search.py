import time
def linear_search(numbers,query):
    #numbers is a list of numbers and query is the value given and we have to find the position of that number in the list
    #function returns the position of the query
    #function returns -1 as the value if the query is not found in the list
    pos  =-1
    for i in range(0,len(numbers)):
        if numbers[i]==query :
            return i
    return pos      

if __name__ == "__main__" :
#to find an element in the list using linear search
    numbers = [1,1,1,1,43,43,43,44,23,21,34,5,434,5435,123,342,32421,34234,53]
    start = time.time()
    print(linear_search(numbers,53))
    end = time.time()
    print("Time required = ",(end-start)*10**3," ms")