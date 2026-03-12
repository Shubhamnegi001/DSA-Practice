#first solution
class Solution:
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        pos = right

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1

        return result

#2nd solution

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = list(map(lambda x: x**2 , nums))
        self.quick_sort(result, 0 , len(result) - 1)
        return result

    def partition(self, result, left, right):
        pivot = result[left]
        i = left
        j = right

        while i < j:
            while i <= right - 1 and result[i] <= pivot:
                i += 1
            while j >= left + 1 and result[j] > pivot:
                j -= 1
            if i < j:
                result[i], result[j] = result[j], result[i]

        result[left], result[j] = result[j], result[left]
        return j

    def quick_sort(self, result, left, right):
        if left < right:
            p_index = self.partition(result, left, right)
            self.quick_sort(result, left, p_index - 1)
            self.quick_sort(result, p_index + 1, right)

#3RD SOLUTION
class Solution:
    def sortedSquares(self, nums):
        self.result = list(map(lambda x:x**2 , nums))
        self.result.sort()
        return self.result

#4th solution
class Solution:
    def sortedSquares(self, nums):
        return sorted([x**2 for x in nums])