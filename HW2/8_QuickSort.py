# Problem Statement:
'''
Using the right sorting technique, sort the double values in the array.

'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print(quick_sort(arr))