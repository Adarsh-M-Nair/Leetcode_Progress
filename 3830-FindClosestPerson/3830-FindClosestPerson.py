# Last updated: 7/18/2026, 8:31:08 PM
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z-x) == abs(z-y):
            return 0
        elif abs(z-x)<abs(z-y):
            return 1
        else:
             return 2