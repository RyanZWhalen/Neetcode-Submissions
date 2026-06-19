class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = []

        for i in range(len(nums)):
            store = target - nums[i]
            list.append(store)

            for j in range(len(nums)):
                if j in list:
                    return [i, j]