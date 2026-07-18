# Last updated: 7/18/2026, 8:32:49 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the current area
            current_height = min(height[left], height[right])
            current_width = right - left
            current_area = current_height * current_width
            
            # Update the maximum area found so far
            max_area = max(max_area, current_area)

            # Move the pointer associated with the shorter line
            # to potentially find a taller line and thus a larger area.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area