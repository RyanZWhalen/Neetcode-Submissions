class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums[i] == nums[i + 1]:
                return true
            else:
                return false