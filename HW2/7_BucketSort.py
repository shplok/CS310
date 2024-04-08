# Problem Statement:
'''
Use bucket sort to organize the temperature values in a range of -50 
to 50 degrees Celsius.

'''


def bucket_sort(tempurature_data):
    if not temperature_data:
        return []

    min_temp = min(temperature_data)
    max_temp = max(temperature_data)
    bucket_sort = 10

    num_buckets = ((max_temp - min_temp) // 5) + 1

    buckets = [[] for _ in range(num_buckets)]

    for temp in temperature_data:
        index = (temp - min_temp) // 5
        buckets[index].append(temp)

    for i in range(num_buckets):
        if buckets[i]:
            buckets[i] = recursive_sort(buckets[i])

    sorted_data = []
    for bucket in buckets:
        sorted_data.extend(bucket)

    return sorted_data


def recursive_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr [1:] if x >= pivot]

    return recursive_sort(left) + [pivot] + recursive_sort(right)



temperature_data = [10, 20, -5, 8, 12, 18, 5, -3, 0, 15]
print(bucket_sort(temperature_data))