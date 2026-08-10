class Node:
    def __init__(self,val):
        self.next = None
        self.val = val
class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    def get(self, index: int) -> int:
        cur = self.head
        if index >= self.size or index < 0 or self.size == 0:
            return -1
        while index > 0:
            cur = cur.next
            index -= 1
        return cur.val
        
        


    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
        else:
            cur = Node(val)
            cur.next = self.head
            self.head = cur
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        if self.size > 0:
            while cur.next:
                cur = cur.next
            cur.next = Node(val)
            self.size += 1

        else:
            self.addAtHead(val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        elif index == self.size:
            self.addAtTail(val)
            return

        cur = self.head
        while index > 1:
            cur = cur.next
            index -= 1
        temp = cur.next
        cur.next = Node(val)
        cur.next.next = temp
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        cur = self.head
        prev = None
        while index > 0:
            prev = cur
            cur = cur.next
            index -= 1
        prev.next = cur.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)