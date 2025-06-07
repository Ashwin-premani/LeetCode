class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        
        pq = []
        
        deleted = set()
        
        for i in range(n):
            if s[i] != '*':
                heapq.heappush(pq, (s[i], -i))
            else:
                while pq:
                    char, neg_idx = heapq.heappop(pq)
                    idx = -neg_idx
                    if idx not in deleted:
                        deleted.add(idx)
                        break
        
        result = ""
        for i in range(n):
            if s[i] != '*' and i not in deleted:
                result += s[i]
                
        return result
