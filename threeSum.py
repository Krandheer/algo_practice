class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, number in enumerate(nums):
            if (i > 0 and number == nums[i-1]):
                continue
            l,r = i+1, len(nums)-1
            
            while(l<r):
                threeSum = number + nums[l] + nums[r]
            
                if (threeSum>0):
                    r = r-1
                elif (threeSum < 0):
                    l = l+1
                else:
                    res.append([number, nums[l], nums[r]])
                    l=l+1
                    while (nums[l]==nums[l-1] and l<r):
                        l=l+1
                    
        return res
        