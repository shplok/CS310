# Problem Statement:
'''
You are given a list of single-letter strings. Implement the Radix Sort 
algorithm to sort the list of strings in lexicographic (dictionary) order.

'''

def radix_sort_char(strings):
    max_len = max(len(s) for s in strings)
    
    for i in range(max_len - 1, -1, -1):
        counting_sort_char(strings, i)

    return strings


def counting_sort_char(strings, index):
    count = [0] * 27  # Increase the size to accommodate both letters and shorter strings
    output = ['' for _ in range(len(strings))]

    for s in strings:
        if index < len(s):
            count[ord(s[index]) - ord('a') + 1] += 1  # Increment at the appropriate index
        else:
            count[0] += 1  # Increment count for shorter strings

    for i in range(1, 27):
        count[i] += count[i - 1]

    i = len(strings) - 1
    while i >= 0:
        if index < len(strings[i]):
            count[ord(strings[i][index]) - ord('a') + 1] -= 1
            output[count[ord(strings[i][index]) - ord('a') + 1]] = strings[i]
        else:
            count[0] -= 1
            output[count[0]] = strings[i]
        i -= 1

    for i in range(len(strings)):
        strings[i] = output[i]


strings = ['d', 'a', 'c', 'b', 'f', 'e']
print(radix_sort_char(strings))
