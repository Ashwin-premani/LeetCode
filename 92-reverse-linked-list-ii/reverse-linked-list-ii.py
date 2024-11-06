# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        dummy = ListNode(0,head)
        cur = head
        left_prev = dummy
        for i in range(left-1):
            left_prev,cur = cur,cur.next
        
        prev = None
        for i in range(right-left+1):
            tmp = cur.next
            cur.next=prev
            prev,cur = cur,tmp
        left_prev.next.next = cur
        left_prev.next = prev

        return dummy.next


