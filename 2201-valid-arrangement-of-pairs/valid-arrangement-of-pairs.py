class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g =  defaultdict(list)
        degree = defaultdict(int)
        path = []

        for s,e in pairs:
            degree[s] += 1
            degree[e] -= 1
            # here starting node will have value 1 since it's never decremented and last node will have -1 and others 0. 
            g[s].append(e)

        start_node = pairs[0][0]
        # to find start node
        for n in degree:
            if degree[n] == 1:
                start_node = n
                break
        def dfs(node):
            while (g[node]):
                next_node = g[node].pop()
                dfs(next_node)
                path.append((node,next_node))
        dfs(start_node)
        return path[::-1]