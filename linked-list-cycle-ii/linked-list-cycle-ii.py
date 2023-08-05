# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        pointer1 = head 
        pointer2 = head
        
        while pointer2 is not None and pointer2.next is not None:
            
            pointer2 = pointer2.next.next
            pointer1 = pointer1.next 
            
            if pointer2 == pointer1:                
                pointer1 = head 
                
                while pointer1 != pointer2:
                    pointer1 = pointer1.next
                    pointer2 = pointer2.next 
                
                return pointer1 
        
        return None