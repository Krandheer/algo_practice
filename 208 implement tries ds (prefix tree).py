class TreeNode:
    def __init__(self, val):
        self.value = val
        self.children={}
        self.isWord = False
    

class Trie:

    def __init__(self):
        self.root = TreeNode(None)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        parent = self.root
        for i, c in enumerate(word):
            if c not in parent.children:
                parent.children[c]=TreeNode(c)
            parent=parent.children[c]
            if i == len(word)-1:
                parent.isWord = True
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        parent = self.root
        for c in word:
            if c not in parent.children:
                return False
            parent = parent.children[c]
        return parent.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        parent = self.root
        for c in prefix:
            if c not in parent.children:
                return False
            parent = parent.children[c]
        return True
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)