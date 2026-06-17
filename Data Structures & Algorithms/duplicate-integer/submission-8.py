"""
Input: array of numbers
Output: boolean T/F value

Space: O(1); should only be T/F value as output
Time: O(n^2); takes n^2 comparisons at worst case scenario
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = []

        for i in len(nums):
            if nums[i] == nums[j]:
                return true
            else:
                return false
        