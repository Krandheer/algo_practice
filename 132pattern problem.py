class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums: 
            return False
        k,stack=float("-inf"),[]
        for number in reversed(nums):
            if number<k:
                return True
            while stack and number>stack[-1]:
                k=stack.pop()
            stack.append(number)
        return False