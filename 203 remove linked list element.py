# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head==None:
            return None
        if head.val==val and head.next ==None:
            return None
        r=ListNode(head.val)
        r2=r
        while(head!=None):
            if head.val == val and head.next == None:
                r.next = None
                head = None 
                break
                
            if head.val==val:
                head=head.next
            else:
                r.next=head
                r=r.next
                head=head.next
        return r2.next
                