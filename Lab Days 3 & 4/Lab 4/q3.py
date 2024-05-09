# Problem Statement:
# Given an array of non-negative integers nums, 
# where each element represents the maximum jump length at that 
# position, determine if you can reach the last index starting from the 
# first index.


def can_jump(nums):
    max_reachable_index = 0
    
    # Iterate through the array
    for i in range(len(nums)):
        # If the current index is beyond the maximum reachable index, return False
        if i > max_reachable_index:
            return False
        # Update the maximum reachable index
        max_reachable_index = max(max_reachable_index, i + nums[i])
        
        # If the maximum reachable index is beyond or at the last index, return True
        if max_reachable_index >= len(nums) - 1:
            return True
    
    return False

# Test the function
nums = [2, 3, 1, 1, 4]
print(can_jump(nums))