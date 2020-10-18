# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        pa=headA
        pb=headB
        d={}
        while pa:
            d[pa]=1
            pa=pa.next
        while pb:
            if pb in d:
                return pb
            pb=pb.next