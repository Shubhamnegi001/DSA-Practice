class Solution:
    def rotate(self, nums):
        n = len(nums)
        k = k % n
        
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


#2nd approach
class Solution:
    def rotate(self, nums):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]

#3RD APPROACH
class Solution:
    def rotate(self, nums):
        n = len(nums)
        k = k % n
        for _ in range (0,k):
            e = nums.pop()
            nums.insert(0,e)