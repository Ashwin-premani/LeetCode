# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []
        cur = l1
        while cur:
            s1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            s2.append(cur.val)
            cur = cur.next
        carry = 0
        res = None

        while s1 or s2 or carry:
            sum = carry
            if s1: sum += s1.pop()
            if s2: sum += s2.pop()

            node = ListNode(sum%10)
            node.next = res
            res = node
            carry = sum // 10
        return res
