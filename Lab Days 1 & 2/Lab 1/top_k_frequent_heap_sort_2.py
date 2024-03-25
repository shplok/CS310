def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # Left = 2*i + 1
    r = 2 * i + 2  # Right = 2*i + 2

    # Check if left child of root exists and is greater than root
    if l < n and arr[l][0] > arr[largest][0]:
        largest = l

    # Check if right child of root exists and is greater than largest so far
    if r < n and arr[r][0] > arr[largest][0]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Heapify the root.
        heapify(arr, n, largest)


def build_heap(arr):
    n = len(arr)
    # Build a max heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def top_k_frequent_elements(arr, k):
    frequency_map = {}
    for num in arr:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Convert frequency_map to a list of tuples (frequency, num)
    freq_list = [(freq, num) for num, freq in frequency_map.items()]

    # Build max heap
    build_heap(freq_list)

    # Extract top k elements
    top_k = []
    for _ in range(k):
        top_element = freq_list[0]
        top_k.append(top_element[1])  # Append the element
        freq_list[0] = freq_list[-1]  # Replace root with last element
        freq_list.pop()  # Remove last element
        heapify(freq_list, len(freq_list), 0)  # Heapify root
    return top_k


# Test the function
arr = [1, 1, 1, 2, 2, 3]
k = 2
result = top_k_frequent_elements(arr, k)
print("Top", k, "frequent elements:", result)
