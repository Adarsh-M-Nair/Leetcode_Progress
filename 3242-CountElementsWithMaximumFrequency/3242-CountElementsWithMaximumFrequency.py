# Last updated: 7/18/2026, 8:31:17 PM
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=Counter(nums)
        maxFreq=0
        sums=0
        for i in c.values():
            if i>maxFreq:
                maxFreq=i
                sums=maxFreq
            elif i==maxFreq:
                sums+=maxFreq
            else:
                continue
        return sums
