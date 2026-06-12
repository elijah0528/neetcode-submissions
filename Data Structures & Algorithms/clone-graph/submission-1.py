"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        q = deque([node])
        clone = {node: Node(node.val)}
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                for neighbor in curr.neighbors:
                    if neighbor not in clone:
                        clone[neighbor] = Node(neighbor.val)
                        q.append(neighbor)
                    clone[curr].neighbors.append(clone[neighbor])
                
        return clone[node]
            
