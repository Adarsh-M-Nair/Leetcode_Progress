# Last updated: 7/18/2026, 8:31:22 PM
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if(n>1 and n%2!=0):
            return n
        elif(n>1 and n%2==0):
            return n//2
        else:
            return 0
        

     