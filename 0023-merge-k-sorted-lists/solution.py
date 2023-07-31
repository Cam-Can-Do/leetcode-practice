# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1, list2):
            dummy = ListNode()
            cur = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            
            if list1:
                cur.next = list1
            if list2:
                cur.next = list2
            return dummy.next
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedList = merge(lists.pop(0), lists.pop(0))
            lists.append(mergedList)
        return lists[0]


