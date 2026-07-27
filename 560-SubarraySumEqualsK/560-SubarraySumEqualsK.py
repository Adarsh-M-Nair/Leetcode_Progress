# Last updated: 7/27/2026, 10:29:00 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        res=0
4        curSum=0
5        prefixSum={0 : 1}
6
7        for n in nums:
8            curSum +=n
9            diff = curSum - k
10
11            res += prefixSum.get(diff,0)
12            prefixSum[curSum] = 1 + prefixSum.get(curSum,0)
13        return res