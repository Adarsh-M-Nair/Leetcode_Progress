# Last updated: 7/18/2026, 8:31:38 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        max_avg=s/k
        for i in range(k,len(nums)):
            s+=nums[i]
            s-=nums[i-k]
            avg=s/k
            max_avg=max(avg,max_avg)
        return max_avg