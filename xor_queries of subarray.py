class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        temp = [arr[0]]
        xor=arr[0]
        for i in range(1,len(arr)):
            xor=arr[i]^xor
            temp.append(xor)
            xor=xor
        for l,h in queries:
            if l==0:
                res.append(temp[h])
            else:
                res.append(temp[h]^temp[l-1])
        return res
            