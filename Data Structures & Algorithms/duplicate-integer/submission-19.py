"""
Input: List of Int
Output: Boolean; T/F Value

Space: O(1); T/F value are constants
Time: O(n^2); at most compare every element to every other element worst-case
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = []

        for i in range(0, len(nums)):
            j = i + 1
            for j in range(1, len(nums)):
                if nums[i] == nums [i + 1]:
                    return True
                else:
                    return False
        