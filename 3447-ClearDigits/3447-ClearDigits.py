# Last updated: 7/18/2026, 8:31:11 PM
class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]>='a' and s[i]<='z' or s[i]>='A' and s[i]<='Z':
                stack.append(s[i])
            else:
                if not stack:
                    return s
                top=stack.pop()
        s1=""
        for i in stack:
            s1+=i
        return s1
