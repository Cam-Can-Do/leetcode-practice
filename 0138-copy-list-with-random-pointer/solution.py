"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None:None}
        # first make a copy of each node mapped to the original 
        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
        
