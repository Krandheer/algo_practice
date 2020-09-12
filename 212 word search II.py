class TrieNode:
    def __init__(self):
        self.word=""
        self.children = {}
        self.isWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or len(board)==0 or not words or len(words)==0:
            return []
        root = TrieNode()
       
        for word in words:
            parent=root
            for letter in word:
                if letter in parent.children:
                    parent=parent.children[letter]
                else:
                    curr_word=parent.word
                    parent.children[letter]= TrieNode()
                    parent=parent.children[letter]
                    parent.word=curr_word+letter
                    
            parent.isWord=True
        
        res=[]
        def backtrack(r, c, node):
            if node.isWord:
                res.append(node.word)
                node.isWord = False
            if r < 0 or r > len(board)-1 or c < 0 or c > len(board[r])-1:
                return
            if board[r][c] not in node.children:
                return
            
            tmpLetter = board[r][c]
            board[r][c] = '$'
            backtrack(r+1, c, node.children[tmpLetter])
            backtrack(r-1, c, node.children[tmpLetter])
            backtrack(r, c+1, node.children[tmpLetter])
            backtrack(r, c-1, node.children[tmpLetter])
            board[r][c] = tmpLetter
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] in root.children:
                    backtrack(r, c, root)
        return res