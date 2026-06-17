"""
"""

def contains_duplicate(nums):
    for i in range(len(nums)):
        if nums[i] == nums[i+1]:
            return true
        else:
            return false
