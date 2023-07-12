# 3. Print all subarrays with 0 sum
# Google Translate Icon
# Given an integer array, print all subarrays with zero-sum.

# For example,

# Input:  { 4, 2, -3, -1, 0, 4 }
 
# Subarrays with zero-sum are
 
# { -3, -1, 0, 4 }
# { 0 }
 
 
# Input:  { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
 
# Subarrays with zero-sum are
 
# { 3, 4, -7 }
# { 4, -7, 3 }
# { -7, 3, 1, 3 }
# { 3, 1, -4 }
# { 3, 1, 3, 1, -4, -2, -2 }
# { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }

def print_zero_sum_subarrays(nums):
    sum_dict = {}

    sum = 0
    for i, num in enumerate(nums):
        sum += num
        if sum == 0:
            print(nums[0:i+1])
        if sum in sum_dict:
            for j in sum_dict[sum]:
                print(nums[j+1:i+1])
        sum_dict.setdefault(sum, []).append(i)

print_zero_sum_subarrays([3, 4, -7, 3, 1, 3, 1, -4, -2, -2])
