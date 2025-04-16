class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l = 0
        n = len(nums)
        pairs = 0
        res = 0
        map = defaultdict(int)
        for r in range(n):
            pairs += map[nums[r]]
            map[nums[r]] += 1

            while pairs >= k:
                res += (n - r)
                map[nums[l]] -= 1
                pairs -= map[nums[l]]
                l += 1
        return res


        #using hash
        n = len(nums)
        hash = defaultdict(int)
        l = 0
        res = 0
        pairs = 0
        for r in range(n):
            # pairs with numbers of occurence of nums[r]
            pairs += hash[nums[r]]
            hash[nums[r]] += 1

            while pairs >= k:
                res += (n - r)
                hash[nums[l]] -= 1
                pairs -= hash[nums[l]]
                l += 1
        return res
