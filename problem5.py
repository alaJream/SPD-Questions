# 5. Find the duplicate element in a limited range array
# Google Translate Icon
# Given a limited range array of size n containing elements between 1 and n-1 with one element repeating, find the duplicate number in it without using any extra space.

# For example,

# Input:  { 1, 2, 3, 4, 4 }
# Output: The duplicate element is 4
 
 
# Input:  { 1, 2, 3, 4, 2 }
# Output: The duplicate element is 2

def find_duplicate(nums):
    return sum(nums) - sum(set(nums))

print(find_duplicate([1, 2, 3, 4, 4]))

