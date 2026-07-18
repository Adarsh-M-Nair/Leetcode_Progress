# Last updated: 7/18/2026, 8:31:07 PM
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        con=""
        s=0
        for i in str(n):
            s+=int(i)
            if i!="0":
                con+=i
            if con=="": return 0
        num=int(con)*s
        
        return num