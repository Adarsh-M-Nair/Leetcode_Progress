# Last updated: 7/18/2026, 8:31:42 PM
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums = sorted(list(set(nums)), reverse=True)
        
        if len(distinct_nums) >= 3:
            return distinct_nums[2]
        else:
            # If fewer than three distinct numbers exist, return the maximum
            return distinct_nums[0]

