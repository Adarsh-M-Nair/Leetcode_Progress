# Last updated: 7/18/2026, 8:32:41 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split()
        last=l[len(l)-1]
        return len(last)

        