class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, j in range(len(nums)) and i < j:
                if nums[i] == nums[j]:
                    return True
        
        return False