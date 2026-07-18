# Last updated: 7/18/2026, 8:31:54 PM
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            b=bin(i)
            sums=0
            for i in b[2:]:
                sums+=int(i)
            ans.append(sums)
        return ans


        