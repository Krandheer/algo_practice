class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows==1:
            return s
        l=len(s)
        
        arr = ["" for x in range(numRows)]
        
        row=0
        for i in range(l):
            arr[row]=arr[row]+s[i]
            
            if row==numRows-1:
                down=False
            
            elif row==0:
                down=True
                
            if down:
                row=row+1
            else:
                row = row-1
        st=''
        for i in range(numRows):
            st=st+arr[i]
        
                
        return st
                
            
            
        