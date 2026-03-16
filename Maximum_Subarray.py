class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = float("-inf")
        current_sum = 0
        for i in range(n):
            current_sum += nums[i]
            max_sum = max(current_sum, max_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum

#2nd approach
class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum
        