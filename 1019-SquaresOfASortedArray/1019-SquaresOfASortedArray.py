# Last updated: 7/18/2026, 8:31:28 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares=[]
        for i in nums:
            squares.append(i**2)
        squares.sort()
        return squares