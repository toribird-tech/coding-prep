from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = curr = ListNode(0)
        while l1 or l2:
            if l1:
                curr.val += l1.val
                l1 = l1.next
            if l2:
                curr.val += l2.val
                l2 = l2.next
            if l1 or l2 or curr.val > 9:
                curr.next = ListNode(1 if curr.val > 9 else 0)
                curr.val %= 10
                curr = curr.next

        return head
