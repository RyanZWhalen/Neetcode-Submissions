class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        target = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in target:
                return [target[diff], i]
            target[nums[i]] = i
        
        return FALSE
