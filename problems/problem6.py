# 6. Find the largest subarray formed by consecutive integers
# Google Translate Icon
# Given an integer array, find the largest subarray formed by consecutive integers. The subarray should contain all distinct values.

# For example,

# Input:  { 2, 0, 2, 1, 4, 3, 1, 0 }
 
# Output: The largest subarray is { 0, 2, 1, 4, 3 }

def largest_consecutive_subarray(nums):
    max_len = 0
    max_subarray = []

    for i in range(len(nums)):
        visited = {}
        dist_count = 0

        for j in range(i, len(nums)):
            if nums[j] in visited:
                break
            else:
                visited[nums[j]] = True
                dist_count += 1

            if dist_count == (max(visited) - min(visited) + 1):
                if dist_count > max_len:
                    max_len = dist_count
                    max_subarray = nums[i:j+1]

    return max_subarray

print(largest_consecutive_subarray([2, 0, 2, 1, 4, 3, 1, 0]))
