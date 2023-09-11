# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1, l2):
            dummy = ListNode()
            cur = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            else:
                cur.next = l2
            return dummy.next
        while len(lists) > 1:
            bucket = []
            bucket.append(lists.pop())
            bucket.append(lists.pop())
            lists.append(mergeTwoLists(bucket[0], bucket[1]))
        if len(lists) > 0:
            return lists[0]
        else:
            return None




        
        
