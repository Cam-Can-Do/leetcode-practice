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
            # get grouping
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev = kth.next
            curr = groupPrev.next
            # reverse group
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
    

                


    def getKth(self, cur, k):
        while k > 0 and cur:
            cur = cur.next
            k -= 1
        return cur






