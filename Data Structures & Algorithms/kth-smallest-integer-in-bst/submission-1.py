# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = None
        def dfs(curr):
            if self.res or self.count > k:
                return

            if curr.left:
                dfs(curr.left)

            self.count += 1
            if self.count == k:
                self.res = curr.val
                return
            if curr.right:
                dfs(curr.right)
            
        dfs(root)
        return self.res
