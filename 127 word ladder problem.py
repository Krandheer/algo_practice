class Solution:
    
    def getWildcard(self, word, i):
        return word[:i] + '*' + word[i + 1:]
    
    def buildWildcardToWords(self, wordList):
        wildcardToWords = {}
        
        for word in wordList:
            for i in range(len(word)):
                wildcard = self.getWildcard(word, i)
                
                if wildcard in wildcardToWords:
                    wildcardToWords[wildcard].append(word)
                else:
                    wildcardToWords[wildcard] = [word]
            
        return wildcardToWords
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wildcardToWords = self.buildWildcardToWords(wordList)
        seen = set()
        
        queue = collections.deque([(beginWord, 1)])
        
        while queue:
            word, level = queue.popleft()
            seen.add(word)
            
            if word == endWord:
                return level
            
            for i in range(len(word)):
                wildcard = self.getWildcard(word, i)
                
                for nextWord in wildcardToWords.get(wildcard, []):
                    if nextWord not in seen:
                            queue.append((nextWord, level + 1))
                            
        return 0