# Last updated: 7/18/2026, 8:32:35 PM
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        for p in path.split('/'):
            if p=='..':
                if stack:
                    stack.pop()
            elif p and p!='.':
                stack.append(p)
        return '/' + '/'.join(stack)
            