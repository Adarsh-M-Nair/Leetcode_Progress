# Last updated: 7/18/2026, 8:32:36 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        else:
           first=1
           second=2
           x=0
           for i in range(2,n):
            x=first+second
            first=second
            second=x
           return x
        