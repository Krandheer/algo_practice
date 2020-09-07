class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        x = numBottles
        while numExchange <= numBottles:
            d, m = divmod(numBottles, numExchange)
            x += d
            numBottles = d + m
        return x
            
        