# Last updated: 7/18/2026, 8:31:34 PM

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicate = -1
        
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        missing = expected_sum - (actual_sum - duplicate)
        return [duplicate, missing]