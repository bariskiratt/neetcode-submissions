# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1,cur2 = l1,l2
        h1,h2 = l1,l2
        count1 = 0
        count2 = 0
        while cur1.next:
            cur1 = cur1.next
            count1 += 1
        while cur2.next:
            cur2 = cur2.next
            count2 += 1
        if count2 > count1:
            h1,h2 = h2,h1
            l1,l2 = l2,l1
        carry = 0
        while h2:
            total = h1.val + h2.val + carry
            carry = total // 10
            total = total - carry * 10
            h1.val = total
            if h1.next == None and carry != 0:
                h1.next = ListNode(carry)
                carry = 0
            h1 = h1.next
            h2 = h2.next
        while carry != 0 and h1.next:
            total = h1.val + carry
            carry = total // 10
            total = total - carry * 10
            h1.val = total
            h1 = h1.next
        if carry != 0:
            total = h1.val + carry
            carry = total // 10
            total = total - carry * 10        
            h1.val = total
            if h1.next == None and carry != 0:
                h1.next = ListNode(carry)
                carry = 0

        return l1


        