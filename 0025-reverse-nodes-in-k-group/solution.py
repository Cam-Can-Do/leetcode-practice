# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            nextGroup = kth.next
            prev = kth.next
            cur = groupPrev.next

            while cur != nextGroup:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next
    
    def getKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
        
