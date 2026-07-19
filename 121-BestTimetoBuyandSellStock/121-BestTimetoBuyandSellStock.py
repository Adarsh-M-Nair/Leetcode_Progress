# Last updated: 7/19/2026, 1:12:09 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        l,r =0, 1 #l for buy and r  for sell
4        maxP=0
5
6        while (r < len(prices)):
7            #profitable?
8            if prices[l] < prices[r]:
9                profit = prices[r] - prices[l]
10                maxP = max(maxP,profit)
11            else:
12                l = r
13            r+=1
14        return maxP