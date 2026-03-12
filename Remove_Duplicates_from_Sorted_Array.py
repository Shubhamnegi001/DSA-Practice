class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        my_dict = {}
        for i in range(n):
            my_dict[nums[i]] = 0
        j = 0
        for x in my_dict:
            nums[j] = x
            j += 1
        return j