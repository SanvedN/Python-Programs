pos = []
def check_occurrence(numbers,query,middle):
    if numbers[middle] == query :
        global pos
        pos.append(middle)
        if middle-1>=0 and numbers[middle-1]==query :
            return 'left'
        else :
            return 'found'
    elif query>numbers[middle] :
        return 'right'
    elif query<numbers[middle] :
        return 'left'
def binary_search(numbers,query):
    numbers = sorted(numbers)
    first = 0
    last = len(numbers)-1
    while first<=last :
        middle = ((first+last)//2)
        res = check_occurrence(numbers,query,middle)
        if res =='found' :
            return middle     
        elif res == 'right' :
            first = middle+1
        elif res == 'left' :
            last = middle-1
    return -1

if __name__ == "__main__" :
    numbers = [1,2,3,1,4,2,5,24]
    print(sorted(numbers))
    print("First Occurrence = ",binary_search(numbers,2))
    print("Occurrences : ",sorted(pos))