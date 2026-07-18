# Last updated: 7/18/2026, 8:31:27 PM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        broken_set = set(brokenLetters) # Convert to a set for efficient lookups
        words = text.split()

        for word in words:
            can_type_word = True
            for char in word:
                if char in broken_set:
                    can_type_word = False
                    break # No need to check further characters in this word
            if can_type_word:
                count += 1
        return count