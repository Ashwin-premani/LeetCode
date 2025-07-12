class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i in range(len(equations)):
            u, v = equations[i]
            val = values[i]
            adj[u].append((v, val))
            adj[v].append((u, 1 / val))
        
        def dfs(src, des, visited, p, ans):
            if src in visited:
                return
            visited.add(src)
            if src == des:
                ans[0] = p
                return
            
            for v, val in adj[src]:
                dfs(v, des, visited, p * val, ans)

        res = []
        for src, des in queries:
            ans = [-1.0]
            prod = 1.0
            if src in adj:
                visited = set()
                dfs(src, des, visited, prod, ans)
            res.append(ans[0])
        
        return res