class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words=str.split(" ")
        pattern1={}
        pattern2={}
        
        if len(pattern)!=len(words):
            return False
        
        for symb, word in zip(pattern, words):
            if symb not in pattern1:
                if word in pattern2:
                    return False
                else:
                    pattern1[symb]=word
                    pattern2[word]=symb
            elif pattern1[symb]!=word:
                return False
        return True