# Last updated: 7/23/2026, 10:03:36 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r =0, 1 #l for buy and r  for sell
        maxP=0

        while (r < len(prices)):
            #profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l = r
            r+=1
        return maxP