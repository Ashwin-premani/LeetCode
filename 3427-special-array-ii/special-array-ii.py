class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        breaks = []

        for i in range(n - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                breaks.append(i)
        
        res = []
        for s, e in queries:
            l = bisect.bisect_left(breaks, s)
            r = bisect.bisect_left(breaks, e) 
            res.append(l == r)
        return res
        # n = len(nums)
        # q = len(queries)
        
        # events = collections.defaultdict(list)
        # for index, (s,e) in enumerate(queries):
        #     events[s].append((index, 1))
        #     events[e].append((index, -1))


        # current = set()
        # res = [False] * q

        # for qi, t in events[0]:
        #     if t == 1:
        #         current.add(qi)
        #     else:
        #         if qi in current:
        #             current.remove(qi)
        #             res[qi] = True

        # for i in range(1, n):
        #     if nums[i] % 2 == nums[i - 1] % 2:
        #         current = set()

        #     for qi, t in events[i]:
        #         if t == 1:
        #             current.add(qi)
        #         else:
        #             if qi in current:
        #                 current.remove(qi)
        #                 res[qi] = True
            
        # return res