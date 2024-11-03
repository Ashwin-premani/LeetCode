# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        l = 0
        tmp = head
        while tmp:
            l+=1
            tmp = tmp.next
        k = k%l
        cur = head
        prev = head
        while k and cur.next:
            cur = cur.next
            k-=1
        while cur.next:
            cur=cur.next
            prev = prev.next
        cur.next = head
        head = prev.next
        prev.next = None
        return head