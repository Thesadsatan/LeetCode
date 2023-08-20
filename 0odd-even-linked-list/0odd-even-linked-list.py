# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        p1 = head 
        p2 = head.next
        tmptail = head.next
        
        while p2 and p2.next:
            nxt = p2.next
            p1.next = nxt 
            p2.next = nxt.next
            nxt.next = tmptail
            p1 = nxt
            p2 = p2.next
        
        return head