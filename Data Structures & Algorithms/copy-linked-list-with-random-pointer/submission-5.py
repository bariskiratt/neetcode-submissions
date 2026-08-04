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
        oldToNew = {None: None}
        if not head:
            return None
        currentOriginal = head.next
        newHead = Node(head.val)
        oldToNew[head] = newHead
        currentCopy = newHead
        while currentOriginal:
            currentCopy.next = Node(currentOriginal.val)
            currentCopy = currentCopy.next
            oldToNew[currentOriginal] = currentCopy
            currentOriginal = currentOriginal.next
        
        cur = head
        copy = newHead
        
        while copy:
            copy.random = oldToNew[cur.random]
            copy = copy.next
            cur = cur.next
        return newHead
        
        

        