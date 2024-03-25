def top_k_frequent(nums, k):
    # Count the frequency of each element
    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    # Find maximum frequency
    max_freq = max(freq_map.values())

    # Create buckets
    buckets = [[] for _ in range(max_freq + 1)]

    # Distribute elements into buckets based on their frequencies
    for num, freq in freq_map.items():
        buckets[freq].append(num)

    # Traverse buckets in reverse order to get top k frequent elements
    top_k_elements = []
    for i in range(max_freq, 0, -1):
        if k > 0 and buckets[i]:
            top_k_elements.extend(buckets[i])
            k -= len(buckets[i])
        if k <= 0:
            break

    return top_k_elements

# Input
arr = [1, 1, 1, 1, 2, 2, 2, 3, 3]
k = 2

# Find top k frequent elements
result = top_k_frequent(arr, k)

# Print the result
print("Top", k, "frequent elements:", result)  # Output: [1, 2]
