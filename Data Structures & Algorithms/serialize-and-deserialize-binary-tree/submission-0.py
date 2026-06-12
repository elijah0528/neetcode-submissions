# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(curr):
            # We are at a leaf node
            if curr is None:
                return "#"
            return f"{curr.val} {dfs(curr.left)} {dfs(curr.right)}"
        
        serialized_tree = dfs(root)
        return serialized_tree

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        it = iter(data.split())

        def dfs():
            v = next(it)
            if v == "#":
                return None
            n = TreeNode(int(v))
            n.left = dfs()
            n.right = dfs()
            return n

        return dfs()