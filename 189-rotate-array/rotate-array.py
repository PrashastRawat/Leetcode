class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        
        # reverse whole array
        nums.reverse()
        
        # reverse first k elements
        nums[:k] = reversed(nums[:k])
        
        # reverse remaining
        nums[k:] = reversed(nums[k:])