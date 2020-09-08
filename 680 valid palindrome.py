class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        
        while l<r:
            if s[l]==s[r]:
                l=l+1
                r = r-1
            else:
                temp1= s[:l]+s[l+1:]
                temp2=s[:r]+s[r+1:]
                
                if temp1==temp1[::-1] or temp2==temp2[::-1]:
                    return True
                else:
                    return False
        return True
                
            
       
        