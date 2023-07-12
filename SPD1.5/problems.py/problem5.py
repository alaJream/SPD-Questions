# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def findNSum(nums: List[int], target: int, N: int, result: List[int], results: List[List[int]]) -> None:
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  
                return

            if N == 2: 
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: 
                for i in range(len(nums) - N + 1): 
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):  
                        findNSum(nums[i+1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        nums.sort()
        findNSum(nums, target, 4, [], results)
        return results
