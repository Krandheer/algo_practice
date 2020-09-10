class Solution:
    def attempt_find_word(self, board, i, j, indx, word):
        if indx == len(word): return True # success!
        if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0: return False #out of bounds
        if board[i][j] != word[indx]: return False #not the correct character
        
        temp = board[i][j] #storing character to undo the change later
        board[i][j] = "-1" #marking cell as seen, to avoid using repeated letters
        
        # explore left, right, up, down
        left = self.attempt_find_word(board, i, j-1, indx+1, word)
        right = self.attempt_find_word(board, i, j+1, indx+1, word)
        up = self.attempt_find_word(board, i-1, j, indx+1, word)
        down = self.attempt_find_word(board, i+1, j, indx+1, word)
        res = left or right or up or down # success?
        
        if not res: board[i][j] = temp #undo the changes because success not reached
        
        return res
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]: #if possible to start from here
                    res = self.attempt_find_word(board, i, j, 0, word)
                    if res: return True #word found
        return False