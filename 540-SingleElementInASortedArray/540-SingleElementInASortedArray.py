# Last updated: 7/18/2026, 8:31:37 PM
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        c=Counter(nums)
        for element,count in c.items():
            if count==1:
                return element