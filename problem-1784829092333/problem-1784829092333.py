# Last updated: 7/23/2026, 11:21:32 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        res = [1] * len(nums)
4
5        prefix=1
6        for i in range(len(nums)):
7            res[i] = prefix
8            prefix *= nums[i]
9        
10        postfix=1
11
12        for i in range(len(nums)-1,-1,-1):
13            res[i] *= postfix
14            postfix *= nums[i]
15        return res