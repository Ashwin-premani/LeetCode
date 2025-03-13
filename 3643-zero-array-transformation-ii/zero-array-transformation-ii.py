class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        # Initialize difference array with n+1 zeros
        diff = [0] * (n + 1)
        sum_val = 0
        pos = 0
        
        for i in range(n):
            # Apply queries until sum + diff[i] >= nums[i]
            while sum_val + diff[i] < nums[i]:
                # Check if we've used all queries
                if pos == len(queries):
                    return -1
                
                start = queries[pos][0]
                end = queries[pos][1]
                val = queries[pos][2]
                pos += 1
                
                # Skip if this query doesn't affect current or future elements
                if end < i:
                    continue
                
                # Apply range update in O(1) using difference array technique
                diff[max(start, i)] += val
                diff[end + 1] -= val
            
            # Update running sum
            sum_val += diff[i]
        
        return pos
        
        n, m=len(nums), len(queries)
        freq=[0]*(n+1)
        op, k=0, 0
        for i in range(n):
            while op<nums[i]-freq[i]:
                if k>=m: 
                    return -1
                l, r, v=queries[k]
                if r<i:
                    k+=1 
                    continue
                freq[max(l, i)]+=v
                freq[r+1]-=v
                k+=1
            op+=freq[i]
        return k

        # Brute Force
        # if all(num == 0 for num in nums):
        #     return 0
            
        # k = 0
        # for i in queries:
        #     l, r, v = i[0], i[1], i[2]
            
        #     for j in range(l, r + 1):
        #         if nums[j] > 0:
        #             nums[j] -= min(v, nums[j])
            
        #     k += 1
            
        #     if all(num == 0 for num in nums):
        #         return k
                
        # return -1