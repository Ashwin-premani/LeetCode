class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if i >= len(candidates) or total > target:
                return 
            cur.append(candidates[i])
            backtrack(i+1, cur, total + candidates[i])
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res





















        res = []
        candidates.sort()  
        
        def dfs(cur, i, total):
            if total == target:
                res.append(cur.copy())  
                return
            if total > target or i >= len(candidates):  
                return 
            
            # Include candidates[i]
            cur.append(candidates[i])
            dfs(cur, i + 1, total + candidates[i])  # Move to the next index
            
            cur.pop()
            
            # Skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
                
            # Exclude candidates[i] and move to the next unique candidate
            dfs(cur, i + 1, total)
                
        dfs([], 0, 0)
        return res