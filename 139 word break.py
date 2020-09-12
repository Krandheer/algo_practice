class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #s-non-empty
        #worddict none-empty list of words
         # the basic things is that when we segment the string s
        # then the last character of s is always a segment present in 
        # if it can be segmented otherwise it can't be segmented

        dp = [False for i in range(len(s)+1)]
        dp[0]=True
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1]=True
        
        return dp[-1]


#Recursive solution:
# def wordbreak(s, worddict):
#     if len(s)==0:
#         return True

#     for x in worddict:
#         result=False
#         prefix=s[0:len(x)]
#         if prefix=x:
#             result=wordbreak(s[len(x):],worddict)
#         if result:
#             return True

#     return False