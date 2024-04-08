# Problem Statement: 
''' In the given decimal array, sort the array using radix sort. '''

def radix_sort_decimal(arr):
    max_exp = 0
    for num in arr:
        exp = 0

        while num // (10 ** exp) > 0:
            exp += 1
        max_exp = max(max_exp, exp)

    for exp in range(max_exp):
        counting_sort_decimal(arr, exp)

    return arr

def counting_sort_decimal(arr, exp):
    n = len(arr)
    
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = int(arr[i] * 10 ** exp) % 10
        count[index] += 1

    
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = int(arr[i] * 10 ** exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


arr = [0.170, 0.45, 0.75, 0.90, 0.802, 0.24, 0.2, 0.66] 
print(radix_sort_decimal(arr))