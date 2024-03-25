def longest_increasing_subsequence(arr):
    n = len(arr)
    if n <= 1:
        return n

    longest_length = 1
    current_length = 1

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            current_length += 1
        else:
            longest_length = max(longest_length, current_length)
            current_length = 1

    # Check if the last element forms part of the longest subsequence
    longest_length = max(longest_length, current_length)

    return longest_length

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
length = longest_increasing_subsequence(arr)
print("Length of longest consecutive increasing subsequence:", length)
