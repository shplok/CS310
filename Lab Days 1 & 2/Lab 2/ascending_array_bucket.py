def bucket_sort(arr):
    # Create Buckets
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Distribute Elements
    for num in arr:
        index = int(num * n)
        buckets[index].append(num)

    # Sort Buckets
    for bucket in buckets:
        bucket.sort()

    # Concatenate sorted buckets
    sorted_arr = [element for sublist in buckets for element in sublist]

    # Update original array
    for i in range(len(arr)):
        arr[i] = sorted_arr[i]

# Input array
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

# Perform bucket sort
bucket_sort(arr)

# Print sorted array
print(arr)  # Output: [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]
