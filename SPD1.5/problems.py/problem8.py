
# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
# You must decrease the overall operation steps as much as possible.

# Example:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # If we know for sure right side is sorted or left side is unsorted
            if nums[mid] < nums[right] or nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # If we know for sure left side is sorted or right side is unsorted
            elif nums[mid] > nums[left] or nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If we get here, that means nums[start] == nums[mid] == nums[end], then shifting out
            # any of the two sides won't change the result but can help remove duplicate from
            # consideration, in this case we just use end-- but left++ works too
            else:
                right -= 1
                
        return False