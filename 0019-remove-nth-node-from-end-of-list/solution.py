# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        if not head or not head.next:
            return None

        # create correctly sized window
        while fast and n > 0:
            fast = fast.next
            n -= 1
        
        # move window to the right until fast is at final node
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

