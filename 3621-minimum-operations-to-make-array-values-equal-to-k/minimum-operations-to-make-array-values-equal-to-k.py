class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # using hash and linear search
        hash = set()
        for i in range(len(nums)):
            if nums[i] < k:
                return -1
            hash.add(nums[i])
        return len(hash) - 1 if k in hash else len(hash)
        
        if all(num == k for num in nums):
            return 0
            
        if any(num < k for num in nums):
            return -1
            
        operations = 0
        
        unique_vals = sorted(set(nums))
        
        while not all(num == k for num in nums):
            max_val = max(nums)
            
            if max_val == k:
                break
                
            h = k
            for val in unique_vals:
                if k <= val < max_val:
                    h = val
            
            for i in range(len(nums)):
                if nums[i] > h:
                    nums[i] = h
            
            operations += 1
            unique_vals = sorted(set(nums))
        
        return operations if all(num == k for num in nums) else -1