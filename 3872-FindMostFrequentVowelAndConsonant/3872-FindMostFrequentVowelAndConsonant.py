# Last updated: 7/18/2026, 8:31:10 PM
from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        # Step 1: Count the frequency of each character in the input string.
        counts = Counter(s)

        # Step 2: Initialize variables to track the maximum frequencies.
        max_vowel_freq = 0
        max_consonant_freq = 0
        vowels = "aeiou"

        # Step 3: Iterate through the character counts to find the maximum frequencies.
        for char, freq in counts.items():
            if char in vowels:
                # If the character is a vowel, update the maximum vowel frequency.
                max_vowel_freq = max(max_vowel_freq, freq)
            else:
                # Otherwise, it's a consonant, so update the maximum consonant frequency.
                max_consonant_freq = max(max_consonant_freq, freq)
        
        # Step 4: Return the sum of the maximum frequencies found.
        return max_vowel_freq + max_consonant_freq

