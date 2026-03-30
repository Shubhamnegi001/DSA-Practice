class Solution:
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            digit = 0
            while num > 0:
                num = num // 10
                digit += 1
            if digit % 2 == 0:
                count += 1
        return count

#2nd
class Solution:
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            digit = 0
            temp = num
            while temp > 0:
                temp = temp // 10
                digit += 1
            if digit % 2 == 0:
                count += 1
        return count

#3rd
class Solution:
    def findNumbers(self, nums):
        count = 0 
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count