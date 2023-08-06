# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        temphead = head
        p1 = head
        p2 = head.next
        
        while p2.next:
            
            p1.next = p2.next
            p2.next = temphead
            temphead = p2
            p2 = p1.next 

        p1.next = p2.next
        p2.next = temphead
        temphead = p2
        
        return temphead