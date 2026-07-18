# Last updated: 7/18/2026, 8:32:13 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        b=bin(n)
        count=0
        for i in b[2:]:
            if i=="1":
                count+=1
        return count