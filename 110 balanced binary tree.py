# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if self.height(root):
            return True
    
    def height(self, root):
        if not root:
            return True
        left_height=self.height(root.left)
        right_height=self.height(root.right)
        if not left_height or not right_height:
            return False
        if (abs(left_height-right_height))>1:
            return False
        return 1+max(left_height, right_height)
    

