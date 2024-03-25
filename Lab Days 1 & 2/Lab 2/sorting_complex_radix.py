import math

def get_magnitude(num):
    return math.sqrt(num[0] ** 2 + num[1] ** 2)

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = int((arr[i][0] / exp) % 10)
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = int((arr[i][0] / exp) % 10)
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(get_magnitude(num) for num in arr)
    exp = 1
    while max_val >= exp:
        counting_sort(arr, exp)
        exp *= 10

def sort_complex_numbers(Complex_Numbers):
    radix_sort(Complex_Numbers)
    return sorted(Complex_Numbers, key=lambda x: (get_magnitude(x), x[0], x[1]))

Complex_Numbers = [(3, 4), (0, 1), (3, 3), (4, 0)]
order = sort_complex_numbers(Complex_Numbers)
print("Result of sorting of the complex numbers:", order)
