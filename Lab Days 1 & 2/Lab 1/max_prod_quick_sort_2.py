# Finding the maximum product
import random

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]

    return i + 1


def quicksort(arr, lo, hi):
    if lo < hi:
        pi = partition(arr, lo, hi)
        quicksort(arr, lo, pi - 1)
        quicksort(arr, pi + 1, hi)


def max_product(arr):

    n = len(arr)
    quicksort(arr, 0, n - 1)

    return max(arr[n - 1] * arr[n - 2], arr[0] * arr[1])

arr = [5, 20, 2, 6, -10, -7]
k = 3

result = max_product(arr)
print(result)


