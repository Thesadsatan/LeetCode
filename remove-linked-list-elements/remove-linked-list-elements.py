# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        temphead = None
        p1 = ListNode()
        p2 = head
        counter = 0
        
        while p2:
            
            if p2.val != val:
                counter +=1
                p1 = p2
                p2 = p2.next 
                if counter == 1:
                    temphead = p1
            else:
                p1.next = p2.next
                p2 = p2.next
                
        return temphead