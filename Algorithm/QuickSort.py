
MyList = [10, 24, 13, 16, 48, 29, 21, 19, 18, 13, 43, 221, 248, 65, 193, 85, 235, 177, 222, 208, 158, 190,576, 206, 757, 140, 70, 577, 396, 723, 661, 304, 339, 280, 613, 610, 669, 764, 49, 463, 170, 370, 92, 113, 450, 155, 210, 653, 233, 373, 641, 194, 65, 361, 399, 273, 21, 531, 114, 562, 611, 202, 666, 386, 127, 401, 500, 213, 279, 526, 27, 52, 340, 325, 364, 389, 802, 615, 545, 268, 282, 665, 41, 415, 78, 308, 528, 503, 414, 109, 485, 360, 743, 668, 192, 360, 589, 152, 332, 477, 44, 654, 808, 100, 403, 672, 244, 360, 692, 787, 18, 836, 819, 359, 403, 484, 496, 367, 141, 787, 81, 220, 715, 272, 357, 180, 545, 144, 722, 9, 259, 160, 803, 163, 845, 564, 126, 26, 396, 285, 203, 573, 555, 674, 160, 16, 794, 146, 862, 692, 147, 514, 807, 451, 502, 840, 768, 338, 492, 790, 101, 466, 533, 2, 5, 844, 774, 632, 282, 740, 592, 197, 152, 525, 390, 889, 344, 441, 834, 338, 861, 682, 742, 775, 922, 95, 663, 173, 476, 846, 561, 803, 133, 787, 503, 286, 146, 842, 896, 919, 191, 452, 778, 734, 208, 431, 62, 786, 866, 213, 166, 612, 958, 16, 877, 761, 675, 451, 47, 160, 491, 874, 778, 954, 6, 866, 199, 562, 136, 354, 86, 930, 676, 913, 564, 484, 704, 339, 71, 79, 463, 458, 909, 401, 161, 657, 322, 0]
test = [54, 34,]

second = [10, 80, 30, 90, 40]
secondSize = len(second) - 1

# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # Choose the rightmost element as pivot
  pivot = array[high]

   # Pointer for greater element
  j = low - 1
  
  # Traverse through all elements
  # compare each element with pivot
  for i in range(low, high):
    if array[i] <= pivot:

      # If element smaller than pivot is found
      # swap it with the greater element pointed by i
      j += 1
      
      # Swapping element at i with element at j 
      (array[j], array[i]) = (array[i], array[j])

    # Swap the pivot element with
    # the greater element specified by i
  (array[j+1], array[high]) = (array[high], array[j+1])

  return j + 1


def quicksort(array, low, high):
  if low < high:
    
    piv = partition(array, low, high)

    quicksort(array, low, piv-1)

    quicksort(array, piv+1, high)
  
  return array

n = len(MyList)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
testLen = len(test)-1
print(quicksort(test, 0, testLen))
         
