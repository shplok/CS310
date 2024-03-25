def counting_sort(arr):
    # Find the maximum value in the array
    max_val = max(arr)
    
    # Create a count array to store the count of each character
    count = [0] * (ord(max_val) - ord('a') + 1)
    
    # Count occurrences of each character
    for char in arr:
        count[ord(char) - ord('a')] += 1

    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([chr(ord('a') + i)] * count[i])

    return sorted_arr

# Test the function
arr = ['b', 'd', 'a', 'c', 'f', 'e']
sorted_arr = counting_sort(arr)
print(sorted_arr)  # Output: ['a', 'b', 'c', 'd', 'e', 'f']
