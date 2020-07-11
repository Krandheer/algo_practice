class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0;
        max_length=1
        for i in range(1, len(s)):
            low = i
            high=i-1
            while(low>=0 and high< len(s) and s[low]==s[high]):
                if (high-low+1>max_length):
                    start = low
                    max_length = high-low +1
                low = low -1
                high = high+1
                
            low = i-1
            high=i+1
            while(low>=0 and high< len(s) and s[low]==s[high]):
                if (high-low+1>max_length):
                    start = low
                    max_length = high-low +1
                low = low-1
                high = high+1
        return s[start:start+max_length]