# Last updated: 7/18/2026, 8:31:14 PM
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        has_vowel=False
        has_consonent=False
        vowels='aeiouAEIOU'

        for i in word:
            if not i.isalnum():
                return False
            if i in vowels:
                has_vowel=True
            elif i.isalpha():
                has_consonent=True
        return has_vowel and has_consonent


        