class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        non_zeroes = []
        for i in range(n):
            if nums[i] != 0:
                non_zeroes.append(nums[i])
        m = len(non_zeroes)
        for j in range(n):
            if j < m:
                nums[j] = non_zeroes[j]
        for i in range(m,n):
            nums[i] = 0
        print(nums)
                

#2nd approach
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1