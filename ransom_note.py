class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashList = [0]*26
        for i in magazine:
            index = ord(i) - ord("a")
            hashList[index] += 1
        for i in ransomNote:
            index = ord(i) - ord("a")
            hashList[index] -= 1
            if hashList[index] < 0:
                return False
        return True

             