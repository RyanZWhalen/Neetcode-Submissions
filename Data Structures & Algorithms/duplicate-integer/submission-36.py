class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            j = i + 1
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    return True
        
        return False