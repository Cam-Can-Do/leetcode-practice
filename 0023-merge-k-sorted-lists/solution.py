# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge lists two at a time


        def mergeTwo(l1, l2):
            dummy = ListNode()
            cur = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next

            if l1:
                cur.next = l1
            elif l2:
                cur.next = l2
            return dummy.next


        if not lists:
            return None

        while len(lists) > 1:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            merged = mergeTwo(l1, l2)
            lists.append(merged)
        
        return lists[0]
