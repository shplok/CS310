# Finding the Kth largest Element


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


def find_kth_largest(arr,k):

    n = len(arr)
    quicksort(arr, 0, n - 1)

    return arr[n - k]

arr = [5, 3, 8, 2, 1, 4]
k = 3

result = find_kth_largest(arr, k)
print(result)


