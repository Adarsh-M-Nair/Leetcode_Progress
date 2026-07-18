# Last updated: 7/18/2026, 8:31:25 PM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        count1=0
        for i in nums:
            count=0
            while i>0:
                rem=i%10
                i//=10
                count+=1
            if count % 2==0:
                count1+=1
        return count1