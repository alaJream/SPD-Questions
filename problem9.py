# Find the maximum product of two integers in an array
# Google Translate Icon
# Given an integer array, find the maximum product of two integers in it.

# For example, consider array {-10, -3, 5, 6, -2}. The maximum product is the (-10, -3) or (5, 6) pair.

def max_product(nums):
    nums.sort()
    return max(nums[0] * nums[1], nums[-1] * nums[-2])

nums = [-10, -3, 5, 6, -2]
print(max_product(nums))