def counting_sort_with_duplicates(arr):
    # Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)
    
    # Create a count array to store the count of each element
    count = [0] * (max_val - min_val + 1)
    
    # Count occurrences of each element
    for num in arr:
        count[num - min_val] += 1

    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr

# Test the function
arr = [3, 5, 1, 9, 3, 8, 1, 2]
sorted_arr = counting_sort_with_duplicates(arr)
print(sorted_arr)  # Output: [1, 1, 2, 3, 3, 5, 8, 9]
