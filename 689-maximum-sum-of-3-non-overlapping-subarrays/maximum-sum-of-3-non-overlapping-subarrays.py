class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # preprocessing
        k_sum = [sum(nums[:k])]
        for i in range(k, len(nums)):
            k_sum.append(k_sum[-1] + nums[i] - nums[i - k])

        dp = {}
        def get_max_sum(i, count):
            if count == 3 or i > len(nums) - k:
                return 0
            if (i, count) in dp:
                return dp[(i, count)]
            # include
            include = k_sum[i] + get_max_sum(i + k, count + 1)

            # skip
            skip = get_max_sum(i + 1, count)

            dp[(i, count)] = max(include, skip)

            return dp[(i, count)]
        
        def get_indices():
            i = 0
            indices = []

            while i <= len(nums) - k and len(indices) < 3:
                include = k_sum[i] + get_max_sum(i + k, len(indices) + 1)
                skip = get_max_sum(i + 1, len(indices))

                if include >= skip:
                    indices.append(i)
                    i += k
                else:
                    i += 1

            return indices

        return get_indices()