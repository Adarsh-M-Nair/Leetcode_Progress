# Last updated: 7/18/2026, 8:31:59 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       n=len(nums)
       expected_sum=n*(n+1)//2
       actual_sum=sum(nums)
       return expected_sum-actual_sum