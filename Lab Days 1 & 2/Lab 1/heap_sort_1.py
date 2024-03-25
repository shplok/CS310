

def heapify(arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def build_min_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def extract_min(arr):
    if not arr:
        return None
    min_element = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    heapify(arr, len(arr), 0)
    return min_element

def find_kth_smallest(arr, k):
    build_min_heap(arr)
    for _ in range(k - 1):
        extract_min(arr)
    return arr[0]

arr = [5, 3, 8, 2, 1, 4]
k = 3
result = find_kth_smallest(arr, k)
print(f"The k th smallest element is:", result)
