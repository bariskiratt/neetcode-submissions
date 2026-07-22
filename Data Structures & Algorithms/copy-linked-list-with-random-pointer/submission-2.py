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
        hashMap = {None:None }
        if not head:
            return None
        currentOriginal = head.next
        newHead = Node(head.val)
        hashMap[head] = newHead
        currentCopy = newHead
                
        while currentOriginal:
            currentCopy.next = Node(currentOriginal.val)
            currentCopy = currentCopy.next
            hashMap[currentOriginal] = currentCopy
            currentOriginal = currentOriginal.next

        cur = head
        while cur:
            currentCopy = hashMap[cur]
            currentCopy.next = hashMap[cur.next]
            currentCopy.random = hashMap[cur.random]
            cur = cur.next
        return newHead






