from typing import Optional
class TreeNode:
    def __init__(self, val):
        self.val: Optional[str] = val
        self.isWord: bool = False
        self.children: Optional[dict[str, TreeNode]] = {}


class PrefixTree:

    def __init__(self):
        self.root = TreeNode(None)

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode(c)
            curr = curr.children[c]
        curr.isWord = True
    
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        if not curr.isWord:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
        