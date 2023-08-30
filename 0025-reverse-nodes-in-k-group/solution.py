# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(node, k):
            while k >0 and node:
                node = node.next
                k -=1
            return node

        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                return dummy.next
            
            groupNext = kth.next
            prev = kth.next
            cur = groupPrev.next
            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next
            
        

        





        
        
