# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        dummy = head
        counter = 0
        
        while dummy is not None:
            counter +=1
            dummy = dummy.next
        
        counter -= n
        
        if counter == 0:
            return head.next
        dummy = head 
        dummy1 = head
        counter1 = 0
        
        while counter != 0:
            counter -=1
            counter1 +=1
            
            if counter1 > 1:                
                dummy = dummy.next
            
            if dummy1 is not None:
                dummy1 = dummy1.next 
        
        
        dummy.next = dummy1.next
        
        return head
        