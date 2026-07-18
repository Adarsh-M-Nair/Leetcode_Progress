# Last updated: 7/18/2026, 8:31:41 PM
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark visited numbers by negating values at corresponding indices
        for num in nums:
            # The number determines the index.
            # Use absolute value in case the number has already been negated.
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] *= -1

        result = []
        # Collect missing numbers based on positive values
        for i, num in enumerate(nums):
            if num > 0:
                result.append(i + 1)
        
        return result

