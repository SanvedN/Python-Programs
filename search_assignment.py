#Question - We have been given a rotated list, we have to identify the minimum number of times the sorted list is rotated
#eg. [5,6,9,0,1,2,3] is the list when [0,1,2,3,5,6,9] is rotated three times
#rotation means adding the last element from the list to the first
#Assume all the entries in the list are unique
def find_rotation_number_using_linear_search(nos) :
    rot = 1
    for i in range(1,len(nos)) :
        if nos[i-1]>nos[i] and nos[i+1]>nos[i] :
            return rot
        else :
            rot += 1
    return 0

def find_rotation_number_using_binary_search(numbers) :
    first = 1
    last = len(numbers)-1
    while first<=last :
        middle = ((first+last)//2)
        if numbers[middle] < numbers[middle-1] :
            return middle
        elif  numbers[middle]>numbers[len(numbers)-1] :
            first = middle+1
        elif numbers[middle]<numbers[len(numbers)-1] :
            last = middle-1
    return 0

if __name__ == "__main__" :
    nos = [5,6,9,0,1,2,3]
    print(find_rotation_number_using_binary_search(nos))
    