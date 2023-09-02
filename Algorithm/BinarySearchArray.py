import math


# binary search function
def doSearch(array, target):
    start = 0
    end = len(array) - 1
    mid = int()

    while(True):
        mid = math.floor((start + end) / 2)

        if array[mid] == target:
            return mid
            
        elif array[mid] < target:
            start = mid + 1

        elif array[mid] > target:
            end = mid - 1

        if start > max:
            return -1




primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]  # noqa

result = doSearch(primes, 59)
print(f"Found prime at index {result}")

