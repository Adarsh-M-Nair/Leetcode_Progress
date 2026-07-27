# Last updated: 7/27/2026, 10:06:53 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        max1=max2=float("-inf")
4
5        for num in nums:
6            if num > max1:
7                max1, max2 = num, max1
8            elif num > max2:
9                max2=num
10        return ((max1-1)*(max2-1))
11