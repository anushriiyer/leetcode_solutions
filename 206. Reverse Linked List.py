# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        new = ListNode(head.val)
        ite = head.next
        while ite:
            old = ListNode(ite.val) #2
            old.next = new
            new = old
            ite = ite.next
          
        return new



        

            
        
