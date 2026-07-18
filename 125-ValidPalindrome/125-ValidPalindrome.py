# Last updated: 7/18/2026, 8:32:26 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=""
        for i in s:
            if i>='a' and i<='z' or i>='A' and i<='Z' or i>='0' and i<='9':
                n+=i
        s=n.lower()
        rev=s[::-1]
        if rev==s:
            return True
        else:
            return False
