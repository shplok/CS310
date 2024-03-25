def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def find_kth_smallest(arr1, arr2, k):
    merged_array = arr1 + arr2
    merge_sort(merged_array)
    return merged_array[k - 1]

# Tests
arr1 = [6, 7, 2, 4]
arr2 = [3, 1, 5]
k = 4
result = find_kth_smallest(arr1, arr2, k)
print(result)  # Output: 4
