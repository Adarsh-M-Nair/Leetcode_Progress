# Last updated: 7/18/2026, 8:32:40 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        l=[]
        for i in digits:
            s+=str(i)
        n=int(s)+1
        for i in str(n):
            l.append(int(i))
        return l

        