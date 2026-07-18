# Last updated: 7/18/2026, 8:32:06 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n &(n-1))==0
        