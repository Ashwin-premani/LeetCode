class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
        
        def dfs(node):
            if node in path:
                return float('inf')
            if node in visit:
                return 0
            visit.add(node)
            path.add(node)
            c = ord(colors[node]) - ord('a')
            count[node][c] = 1
            for nei in adj[node]:
                if dfs(nei) == float('inf'):
                    return float('inf')
                for i in range(26):
                    count[node][i] = max(count[node][i], (1 if i == c else 0) + count[nei][i])
            path.remove(node)
            return max(count[node])
            
        n, res = len(colors), 0
        visit, path = set(), set()
        count = [[0] * 26 for i in range(n)] # node, color -> max freq color
        for i in range(n):
            res = max(dfs(i), res)
        
        return -1 if res == float('inf') else res