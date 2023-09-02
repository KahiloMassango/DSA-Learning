tester = [6, 3, 5, 9, 2, 10, 14]
second = [2, 3, 5, 6, 9, 10, 14]

def swapNext(array, a):
    temp = array[a]
    array[a] = array[a+1]
    array[a+1] = temp
    return array

test = [1, 2]
def bubbleSort(mylist):
    length = range(len(mylist) - 1)
    for j in length:
        for i in length:
            if mylist[i] > mylist[i+1]:
                swapNext(mylist, i)   
    return mylist

print(bubbleSort(second))