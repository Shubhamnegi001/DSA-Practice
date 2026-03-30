class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        result = [0]*n
        pos_index = 0
        neg_index = 1
        for num in nums:
            if num > 0:
                result[pos_index] = num
                pos_index += 2
            else:
                result[neg_index] = num
                neg_index += 2
        return result
    
#2nd
class Solution:
    def rearrangeArray(self, nums):
        positive_nums = []
        negative_nums = []
        for i in nums:
            if i > 0:
                positive_nums.append(i)
            else:
                negative_nums.append(i)
        n = len(positive_nums)
        rearrange_nums = []
        for i in range(n):
            rearrange_nums.append(positive_nums[i])
            rearrange_nums.append(negative_nums[i])
        return rearrange_nums