# Last updated: 7/18/2026, 8:31:52 PM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Handle non-positive numbers as they cannot be powers of four
        if n <= 0:
            return False
        
        # Handle the base case: 1 is 4^0
        if n == 1:
            return True
        
        # Continuously divide by 4 as long as it's divisible
        # If n is a power of four, it will eventually become 1
        while n % 4 == 0:
            n //= 4
            
        # If n is 1 after repeated division, it was a power of four
        return n == 1