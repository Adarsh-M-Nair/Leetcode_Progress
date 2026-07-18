# Last updated: 7/18/2026, 8:32:53 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]