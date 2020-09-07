class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i=0
        j=0
        count=0
        g.sort()
        s.sort()
        
        while (i<len(g) and j<len(s)):
            if g[i]<=s[j]:
                i=i+1
                j=j+1
                count=count+1
                
            elif(g[i]>s[j]):
                j = j+1
                
        return count
                
        