# Last updated: 7/18/2026, 8:32:50 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        rev=s[::-1]
        if rev==s:
            return True
        else:
            return False