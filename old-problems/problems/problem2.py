# 2. Check if a subarray with 0 sum exists or not
# Google Translate Icon
# Given an integer array, check if it contains a subarray having zero-sum.
# Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
 
# Output: Subarray with zero-sum exists
 
# The subarrays with a sum of 0 are:
 
# { 3, 4, -7 }
# { 4, -7, 3 }
# { -7, 3, 1, 3 }
# { 3, 1, -4 }
# { 3, 1, 3, 1, -4, -2, -2 }
# { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

def zero_sum_subarray(nums):
    sum_set = set()

    sum = 0
    for num in nums:
        sum += num
        if sum in sum_set or sum == 0:
            return "Subarray with zero-sum exists"
        sum_set.add(sum)

    return "No subarray with zero-sum exists"

print(zero_sum_subarray([3, 4, -7, 3, 1, 3, 1, -4, -2, -2]))
