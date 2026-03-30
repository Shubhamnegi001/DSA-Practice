class Solution:
    def singleNumber(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] not in nums[:i] + nums[i+1:]:
                return nums[i]

#2nd 
class Solution:
    def singleNumber(self, nums):
        nums.sort()
        n = len(nums)
        i = 0
        while i < n - 1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        
        if i == n - 1:
            return nums[i]

#3rd
class Solution:
    def singleNumber(self, nums):
        single = 0
        for num in nums:
            single = single ^ num
        
        return single
        