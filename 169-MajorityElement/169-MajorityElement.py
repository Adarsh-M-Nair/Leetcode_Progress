# Last updated: 7/18/2026, 8:32:16 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        majority_element = None
        max_count = 0  # Initialize max_count to 0

        for element, count in c.items(): # Iterate through (element, count) pairs
            if count > max_count:
                max_count = count
                majority_element = element
                
        return majority_element