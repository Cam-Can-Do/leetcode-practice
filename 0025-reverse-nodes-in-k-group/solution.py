# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            kth = self.getKth(prevGroup, k)
            if not kth:
                break
            nextGroup  = kth.next

            prev = kth.next
            cur = prevGroup.next
            while cur != nextGroup:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp
        return dummy.next

    def getKth(self, node, k):
        while k > 0 and node:
            node = node.next
            k -= 1
        return node


    
        
