class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # using factorial we can find nth perm with out recursion
        #for eg for n = 4 and k = 16th we can go to 3rd num [1,2,3,4] since it has 12-17 perms and then (3 + {1,2,4})16%6 = 4 (3!) means last perms (we picked 4)  (4 + {1,2})and then 4 % 2(2!) which gives 1 + {2} and then 0 % 1 (1!) which gives 2 and ans is [3,4,1,2]
        
        fact = 1
        nums = []
        for i in range(1, n):
            fact *= i
            nums.append(i)
        nums.append(n)
        ans = ''
        k = k - 1
        while True:
            ans += str(nums[k//fact])
            nums.pop(k//fact)
            if len(nums) == 0:
                break
            k %= fact
            fact //= len(nums)

        return ans
        # failed try
        # num = [i for i in range(1, n + 1)]
        
        # def backtrack(i, k, perm):
        #     if len(perm) == n:
        #         k -= 1
        #     if k == 0 and len(perm) == n:
        #         return ''.join(map(str, perm))
            
        #     for j in range(i, n):
        #         perm.append(num[j])
        #         result = backtrack(j + 1, k, perm)
        #         if result: 
        #             return result
        #         perm.pop()  

        # return backtrack(0, k, [])


        # brute force - use recursion ad save and sort all permutations in data structure and return [k-1], time complexity O(n! * n ) and sorting O(n!n log(n!n))