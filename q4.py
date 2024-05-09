def tropical_sort(arr):
    stack = []
    for num in arr:
        if not stack or num <= stack[-1]:
            stack.append(num)  # If the stack is empty or the current number is less than or equal to the top of the stack, push the number onto the stack.
        else:
            idx = len(stack) - 1
            while idx >= 0 and stack[idx] < num:
                idx -= 1  # Find the correct position to insert the current number by iterating through the 
                        # stack from the top until we find a number greater than or equal to the current number.
            stack.insert(idx + 1, num)  # Insert the current number at the correct position in the stack.
    return stack

arr = [4, 7, 2, 5]
sorted_arr = tropical_sort(arr)
print(sorted_arr[::-1])  # Output: [2, 4, 5, 7]
