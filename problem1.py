# 1. Find a pair with the given sum in an array
# Google Translate Icon
# Given an unsorted integer array, find a pair with the given sum in it.
# For example,

# Input:
 
# nums = [8, 7, 2, 5, 3, 1]
# target = 10
 
# Output:
 
# Pair found (8, 2)
# or
# Pair found (7, 3)
 
 
# Input:
 
# nums = [5, 2, 6, 8, 1, 9]
# target = 12
 
# Output: Pair not found


def find_pair(nums, target):
    pair_set = set()
    
    for num in nums:
        if target - num in pair_set:
            return (target - num, num)
        pair_set.add(num)
    
    return "Pair not found"

print(find_pair([8, 7, 2, 5, 3, 1], 10))
