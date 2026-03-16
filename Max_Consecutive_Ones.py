class Solution:
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        count = 0
        max_count = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                max_count = max(max_count,count)
                count = 0
        result = max(count,max_count)
        return result
    

#2nd approach
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        count = 0
        max_count = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                max_count = max(max_count,count)
                count = 0
        return max(count,max_count)