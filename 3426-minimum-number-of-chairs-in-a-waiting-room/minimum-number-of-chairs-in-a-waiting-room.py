class Solution:
    def minimumChairs(self, s: str) -> int:
        chair=0
        m=0
        for char in s:
            if char=='E':
                chair+=1
            elif char=='L':
                chair-=1
            m=max(m,chair)
        return m

