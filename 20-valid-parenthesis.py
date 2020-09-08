class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left=["(","{", "["]
        right=[")","}", "]"]
        
        for paren in s:
            if paren in left:
                stack.append(paren)
            elif paren in right:
                if len(stack)<=0:
                    return False
                elif(right.index(paren)!=left.index(stack.pop())):
                        return False
                
       
        return len(stack)==0