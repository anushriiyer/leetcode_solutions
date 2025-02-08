'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        store = []
        curr = head
        while curr:
            store.append(curr) #put the node itself into the list
            curr = curr.next
        
        if len(store)<=n:
            return head.next
        
        prev = store[len(store)-n-1] #access the node via the list 
        prev.next = prev.next.next #point the node.next to node.next.next
        
        return head
