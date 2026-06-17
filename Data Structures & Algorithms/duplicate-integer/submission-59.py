class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        
        return False