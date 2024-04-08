# Problem Statement:
''' 
Given an array of characters representing lowercase English letters, sort the array alphabetically
using Counting Sort.

'''


def counting_sort_lower(arr):
    count = [0] * 26
    for char in arr:
        count[ord(char) - ord('a')] += 1
        # incrementing each count at the given unicode value for string

    sorted_arr = []
    for i in range(26):
        sorted_arr.extend([chr(i + ord('a'))] * count[i])
    
    return sorted_arr



arr = ['b', 'd', 'a', 'c', 'f', 'e']
print(counting_sort_lower(arr))

