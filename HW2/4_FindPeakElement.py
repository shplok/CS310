# Problem Statement:
''' 
You are given an array of integers representing a mountain, where adjacent elements are in increasing order 
until a peak is reached. After which adjacent elements are in decreasing order.
Find the peak element and return its index.

'''

def find_peak(mountain):

    left = 0
    right = len(mountain) - 1

    while left < right:
        mid = (left + right) // 2
        if mountain[mid] < mountain[mid + 1]:
            left = mid + 1
        else:
            right = mid 
    return left


mountain = [1, 3, 5, 4, 2]
print(find_peak(mountain))