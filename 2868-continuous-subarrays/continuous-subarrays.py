class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        # min and max monotonic queues
        minq = collections.deque()
        maxq = collections.deque()
        left = 0
        for right in range(n):
            x = nums[right]
            while len(minq) > 0 and minq[-1] > x:
                minq.pop()
            minq.append(x)

            while len(maxq) > 0 and maxq[-1] < x:
                maxq.pop()
            maxq.append(x)
            # minq[0] is min element
            # maxq[0] is max element

            # left to right inclusive is hwere minq and maxq operates
            while maxq[0] - minq[0] > 2:
                y = nums[left]
                if minq[0] == y:
                    minq.popleft()
                if maxq[0] == y:
                    maxq.popleft()
                left += 1
            # from left to rigth all pairs are <= 2
            res += (right - left + 1)
        return res