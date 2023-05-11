# 7. Find maximum length subarray having a given sum
# Google Translate Icon
# Given an integer array, find the maximum length subarray having a given sum.

# For example, consider the following array:

# nums[] = { 5, 6, -5, 5, 3, 5, 3, -2, 0 }
# target = 8
 
 
# Subarrays with sum 8 are
 
# { -5, 5, 3, 5 }
# { 3, 5 }
# { 5, 3 }
 
# The longest subarray is { -5, 5, 3, 5 } having length 4

def max_length_subarray(nums, target):
    sum_dict = {}
    sum = 0
    max_len = 0
    max_subarray = []

    for i, num in enumerate(nums):
        sum += num
        if sum == target:
            max_len = i + 1
            max_subarray = nums[:i+1]
        elif (sum - target) in sum_dict:
            if max_len < i - sum_dict[sum - target]:
                max_len = i - sum_dict[sum - target]
                max_subarray = nums[sum_dict[sum - target] + 1:i+1]
        if sum not in sum_dict:
            sum_dict[sum] = i

    return max_subarray

print(max_length_subarray([5, 6, -5, 5, 3, 5, 3, -2, 0], 8))
