# Last updated: 7/18/2026, 8:32:12 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        q=deque([root])
        while q:
            lev_len=len(q)
            for i in range(lev_len):
                p=q.popleft()
                if i==(lev_len-1):
                    res.append(p.val)
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)

        return res