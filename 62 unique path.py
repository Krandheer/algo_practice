class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x=m+n-2
        
        return self.factorial(x)//(self.factorial(m-1)*self.factorial(n-1))
        
    def factorial(self,n):
        if(n==0):
            return 1
        else:
            return n*factorial(n-1)
        