# Last updated: 7/18/2026, 8:31:12 PM
class Solution:
    def maxDifference(self, s: str) -> int:
        char_count=Counter(s)
        odd=[]
        even=[]
        for i in char_count.values():
            if i % 2==0:
                even.append(i)
            else:
                odd.append(i)
        max_odd=max(odd)
        min_even=min(even)
        return max_odd-min_even


