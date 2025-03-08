class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def findCombinations(ind, arr, target, ans, ds):
            if target == 0:
                ans.append(ds.copy())
                return
            
            for i in range(ind, len(arr)):
                # Skip duplicates
                if i > ind and arr[i] == arr[i-1]:
                    continue
                # If current element exceeds target, break
                if arr[i] > target:
                    break
                    
                # Include current element
                ds.append(arr[i])
                # Recursive call with next index, reduced target
                findCombinations(i+1, arr, target - arr[i], ans, ds)
                # Backtrack
                ds.pop()
            
        # Initialize result list
        ans = []
        # Sort candidates to handle duplicates properly
        candidates.sort()
        # Start recursive process
        findCombinations(0, candidates, target, ans, [])
        return ans



        # res = []
        # candidates.sort()
        # def backtrack(i, cur, total):
        #     if total == target:
        #         res.append(cur.copy())
        #         return 
        #     if i >= len(candidates) or total > target:
        #         return 
        #     cur.append(candidates[i])
        #     backtrack(i+1, cur, total + candidates[i])
        #     cur.pop()
        #     while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
        #         i += 1
        #     backtrack(i + 1, cur, total)

        # backtrack(0, [], 0)
        # return res


        # res = []
        # candidates.sort()  
        
        # def dfs(cur, i, total):
        #     if total == target:
        #         res.append(cur.copy())  
        #         return
        #     if total > target or i >= len(candidates):  
        #         return 
            
        #     # Include candidates[i]
        #     cur.append(candidates[i])
        #     dfs(cur, i + 1, total + candidates[i])  # Move to the next index
            
        #     cur.pop()
            
        #     # Skip duplicates
        #     while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
        #         i += 1
                
        #     # Exclude candidates[i] and move to the next unique candidate
        #     dfs(cur, i + 1, total)
                
        # dfs([], 0, 0)
        # return res