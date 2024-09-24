class Solution(object):
    def copyRandomList(self, head):
        oldtoCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldtoCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldtoCopy[cur]
            copy.next = oldtoCopy[cur.next]
            copy.random = oldtoCopy[cur.random]
            cur = cur.next

        return oldtoCopy[head]