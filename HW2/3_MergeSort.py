# Problem Statement:
''' 
You are given k sorted lists of integers. Implement the merge sort algorithm
merge k lists into a single sorted list.

'''

def merge_k_lists(lists):
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]
    
    mid = len(lists) // 2
    left_lists = merge_k_lists(lists[:mid])
    right_lists = merge_k_lists(lists[mid:])

    return merge_sorted_lists(left_lists, right_lists)


def merge_sorted_lists(l, r):
    result = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    result.extend(l[i:])
    result.extend(r[j:])

    return result



k = 3
lists =[[1, 4, 6], [2, 3, 5], [0, 7, 8]]


print(merge_k_lists(lists))