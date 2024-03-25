# find the missing mnumber in an array of consecutive numbers

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key


def find_missing_number(arr):
    insertion_sort(arr)
    for i in range(len(arr) - 1):
        if arr[i] + 1 != arr[i + 1]:
            return arr[i] + 1
    return None

arr = [1, 2, 3, 5, 6, 7, 8,]
missing_number = find_missing_number(arr)
print("Missing Number: ", missing_number)