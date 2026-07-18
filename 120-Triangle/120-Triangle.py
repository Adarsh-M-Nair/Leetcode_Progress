# Last updated: 7/18/2026, 8:32:27 PM
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        # Start from the second to last row and move upwards.
        # This can be done in-place or with a 1D DP array for space efficiency.
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                # For each element, update its value with the minimum
                # path sum from itself to the bottom.
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        
        # The top of the triangle now holds the minimum total sum.
        return triangle[0][0]