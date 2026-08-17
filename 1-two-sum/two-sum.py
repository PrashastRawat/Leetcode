class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            total  = target - nums[i]
            if total in seen:
                return (seen[total],i)
            seen[nums[i]] = i