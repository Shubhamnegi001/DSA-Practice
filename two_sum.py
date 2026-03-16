from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]   
                


#2nd approach
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_map = {}
        for i in range(n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return (hash_map[remaining],i)
            hash_map[nums[i]] = i  