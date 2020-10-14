class Solution:
    
    def getWildcard(self, word, i):
        return word[:i] + '*' + word[i + 1:]
    
    #this build adjancy list of word differing by one letter
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
    
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        
        wildcardToWords = self.buildWildcardToWords(wordList)
        
        #seen will ensure if visited or not
        seen = set()
        
        #this queue will help to do the bfs traversal
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