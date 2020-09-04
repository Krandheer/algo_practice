class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_length = max(len(a), len(b))
        a=a.zfill(max_length)
        b=b.zfill(max_length)
        
        result = ""
        carry=0
        for i in range(max_length-1,-1,-1):
            sum = int(a[i])+int(b[i])+carry
            if(sum%2==1):
                result="1"+result
            else:
                result="0"+result
            if(sum>1):
                carry=1
            else:
                carry = 0
        if (carry!=0):
            result = "1"+result
        return result.zfill(max_length)
            