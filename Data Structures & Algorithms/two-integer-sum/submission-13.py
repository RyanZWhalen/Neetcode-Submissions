class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            diff.store(difference)

            for j in range(len(nums)):
                if j in list:
                    return [i,j]