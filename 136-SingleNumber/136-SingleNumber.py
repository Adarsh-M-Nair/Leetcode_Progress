# Last updated: 7/18/2026, 8:32:25 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)==1:
                return i
        