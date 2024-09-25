# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ret_cur = head
        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                ret_cur.next = cur1
                cur1 = cur1.next
            else:
                ret_cur.next = cur2
                cur2 = cur2.next
            ret_cur = ret_cur.next
        
        while cur1:
            ret_cur.next = cur1
            cur1 = cur1.next
            ret_cur = ret_cur.next
        while cur2:
            ret_cur.next = cur2
            cur2 = cur2.next
            ret_cur = ret_cur.next
        return head.next
