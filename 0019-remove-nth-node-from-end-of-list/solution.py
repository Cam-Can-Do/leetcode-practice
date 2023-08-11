# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)
        
        
        l = dummy
        r = dummy
        while n > 0:
            r = r.next
            n -= 1
        
        while r and r.next:
            r = r.next
            l = l.next
        l.next = l.next.next
        return dummy.next


        
