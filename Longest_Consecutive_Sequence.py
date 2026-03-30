class Solution:
    def longestConsecutive(self, nums):
        nums.sort()
        n = len(nums)
        count = 0
        last_smaller = float("-inf")
        longest = 0
        for i in range(n):
            num = nums[i]
            if num - 1 == last_smaller:
                count += 1
                last_smaller = num
            elif num != last_smaller:
                count = 1
                last_smaller = num
            longest = max(longest,count)
        return longest

#2nd
class Solution:
    def longestConsecutive(self, nums):
        my_set = set(nums)
        longest = 0
        for num in my_set:
            if num - 1 not in my_set:
                x = num
                count = 1
                while x + 1 in my_set:
                    count += 1
                    x += 1
                longest = max(longest, count)
        return longest