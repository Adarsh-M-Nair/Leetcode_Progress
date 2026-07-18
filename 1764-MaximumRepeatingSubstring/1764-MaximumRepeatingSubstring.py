# Last updated: 7/18/2026, 8:31:23 PM
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0  # Represents the current number of consecutive repetitions
        max_k = 0 # Stores the maximum consecutive repetitions found so far
        
        while word * (k + 1) in sequence: # Check if (k+1) repetitions exist
            k += 1 # If yes, increment k
            max_k = k # Update max_k
            
        return max_k