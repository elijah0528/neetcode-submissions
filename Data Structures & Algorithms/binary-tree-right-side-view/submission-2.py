# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []
        if root is None:
            return res
        while q:
            size = len(q)
            is_appended = False
            for _ in range(size):
                curr = q.popleft()
                if not is_appended:
                    res.append(curr.val)
                    is_appended = True
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
        return res