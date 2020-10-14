# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        min_depth=float('inf')
        q = collections.deque([(1,root)])
        while q:
            children=[]
            for i in range(len(q)):
                level, node=q.popleft()
                if not node.left and not node.right:
                    return min(level, min_depth)
                if node.left:
                    children.append((level+1, node.left))
                if node.right:
                    children.append((level+1, node.right))
            q.extend(children)
                
        return min_depth
            
            
            
        