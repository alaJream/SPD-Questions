# 4. Sort binary array in linear time
# Google Translate Icon
# Given a binary array, sort it in linear time and constant space. The output should print all zeroes, followed by all ones.

# For example,

# Input:  { 1, 0, 1, 0, 1, 0, 0, 1 }
 
# Output: { 0, 0, 0, 0, 1, 1, 1, 1 }

def sort_binary_array(nums):
    zero_count = nums.count(0)
    one_count = len(nums) - zero_count
    return [0]*zero_count + [1]*one_count

print(sort_binary_array([1, 0, 1, 0, 1, 0, 0, 1]))
