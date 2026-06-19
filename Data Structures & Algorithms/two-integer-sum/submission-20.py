class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_diff = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in target_diff:
                return [target_diff[diff], i]
            target_diff.update(nums[i])
        return None