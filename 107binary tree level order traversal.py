# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        mydict={}
        
        queue=collections.deque()
        level=collections.deque()
        
        if not root:
            return []
        
        queue.append(root)
        level.append(0)
        
        count=0
        
        while queue:
            cur=queue.popleft()
            count=level.popleft()
            
            if count not in mydict:
                mydict[count]=[]
            mydict[count]+= [cur.val]
            
            if cur.left:
                queue.append(cur.left)
                level.append(count+1)
            if cur.right:
                queue.append(cur.right)
                level.append(count+1)
        print(mydict)
        
        mylist = []
        
        for val in mydict.values():
            mylist.append(val)

        return mylist[::-1]