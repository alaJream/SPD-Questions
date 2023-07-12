# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# # Example:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

class Solution(object):
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triples = set()
        nums.sort()
        for i in range(len(nums)):
            num1, num2 = i + 1, len(nums) -1
            while num1 < num2:
                if nums[i] + nums[num1] + nums[num2] == 0:
                    triples.add((nums[i], nums[num1], nums[num2]))
                    num1 += 1
                    num2 -= 1
                elif nums[i] + nums[num1] + nums[num2] > 0:
                    num2 -= 1
                else:
                    num1 += 1
        return triples