# Last updated: 7/18/2026, 8:31:40 PM
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower():
            return True
        if word.isupper():
            return True
        if word[0].isupper() and word[1:].isupper() or word[1:].islower():
            return True
        else:
            return False
        
        