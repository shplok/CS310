# Problem Statement:
''' 
Given an array of integers containing duplicate elements, sort the array using Counting Sort 
while preserving order of duplicates

'''

def counting_sort_duplicates(arr):
    count = [0] * (max(arr) + 1)
    for num in arr:
        count[num] += 1
        # incrementing each count at the given unicode value for string

    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr



arr = [3, 5, 1, 9, 3, 8, 1, 2]
print(counting_sort_duplicates(arr))