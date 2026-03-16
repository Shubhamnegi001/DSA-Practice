class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
            

#2nd approach
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        my_dict = {i: 0 for i in range(n+1)}
        
        for num in nums:
            my_dict[num] = 1
        
        for k, v in my_dict.items():
            if v == 0:
                return k

#3rd approach
class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return (n * (n + 1) // 2) - sum(nums) 
                