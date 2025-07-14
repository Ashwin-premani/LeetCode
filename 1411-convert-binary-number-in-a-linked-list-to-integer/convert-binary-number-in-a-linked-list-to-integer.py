# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        l = 0
        res = 0
        s = []
        root = head
        while root:
            s.append(root.val)
            root = root.next
        
        for i in range(len(s) - 1, -1 , -1):
            if s[i] == 1:
                res += (2**l)
            l += 1
        return res