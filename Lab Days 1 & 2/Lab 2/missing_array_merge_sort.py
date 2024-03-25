def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_half = [0] * n1
    right_half = [0] * n2

    for i in range(0, n1):
        left_half[i] = arr[left + i]
    for j in range(0, n2):
        right_half[j] = arr[mid + 1 + j]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def find_missing_number(arr):
    n = len(arr)
    merge_sort(arr, 0, n - 1)

    # Expected sum of consecutive numbers
    expected_sum = (n + 1) * (n + 2) // 2

    # Actual sum of elements in the array
    actual_sum = sum(arr)

    # The missing number will be the difference between the expected sum and the actual sum
    missing_number = expected_sum - actual_sum
    return missing_number

# Test the function
arr = [1, 5, 3, 6, 8, 7, 2]
missing_number = find_missing_number(arr)
print("Missing number:", missing_number)  # Output: 4
