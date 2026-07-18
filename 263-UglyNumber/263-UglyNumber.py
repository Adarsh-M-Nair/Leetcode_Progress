# Last updated: 7/18/2026, 8:32:00 PM
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:  # Ugly numbers are positive integers
            return False
        
        # Divide by 2, 3, and 5 repeatedly
        for prime in [2, 3, 5]:
            while n % prime == 0:
                n //= prime
        
        # If n becomes 1, it's an ugly number
        return n == 1


            
        