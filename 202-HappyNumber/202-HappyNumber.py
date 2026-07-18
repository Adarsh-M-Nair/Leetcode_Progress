# Last updated: 7/18/2026, 8:32:10 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # To detect cycles
        
        while n != 1 and n not in seen:
            seen.add(n)
            current_sum_of_squares = 0
            temp_n = n  # Use a temporary variable to extract digits
            while temp_n > 0:
                digit = temp_n % 10
                current_sum_of_squares += digit * digit
                temp_n //= 10
            n = current_sum_of_squares  # Update n with the new sum
            
        return n == 1