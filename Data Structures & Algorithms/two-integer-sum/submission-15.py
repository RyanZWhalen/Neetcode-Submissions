class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_diff = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in diff:
                return [diff[target_diff], i]
            else:
                diff.update(nums[i])


        return None