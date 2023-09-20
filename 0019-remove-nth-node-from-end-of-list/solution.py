# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        front = head
        while n > 0:
            front = front.next
            n -= 1
        back = dummy
        while front:
            back = back.next
            front = front.next

        # front.next is now the node that needs to be removed
        back.next = back.next.next # change link in the singly-linked list
        return dummy.next

