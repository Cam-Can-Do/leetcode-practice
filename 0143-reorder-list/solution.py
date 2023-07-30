# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first need to find the middle of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        # break the link between the halves, setup for reversing second half
        second = slow.next
        slow.next = prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # now we have prev storing the head of the second list, and head storing the head of the first
        # need to alternate (starting with first list) and join the links together
        first = head
        second = prev
        while second:
            cur1 = first.next
            cur2 = second.next
            first.next = second
            second.next = cur1
            first = cur1
            second = cur2
        
