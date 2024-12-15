import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for passed, total in classes:
            heapq.heappush(heap, (-self.profit(passed, total), passed, total))
        
        for _ in range(extraStudents):
            profit, passed, total = heapq.heappop(heap)
            
            heapq.heappush(heap, (-self.profit(passed + 1, total + 1), passed + 1, total + 1))
        
       
        return sum(p / t for _, p, t in heap) / len(classes)
    
    def profit(self, passed, total):
       
        return (passed + 1) / (total + 1) - passed / total