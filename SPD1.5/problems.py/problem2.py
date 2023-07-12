#  Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.


class Solution(object):
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]