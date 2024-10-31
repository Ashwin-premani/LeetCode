class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        r = len(robot)
        factory.sort()
        f = len(factory)
        inf = 10**30

        @cache
        def go(ri,fi):
            if fi == f:
                return inf
            best = inf
            cost = 0

            for i in range(factory[fi][1]+1):
                if ri+i >=r:
                    best = min(best , cost)
                    break
                best = min(best, go(ri+i,fi+1)+cost)
                cost += abs(factory[fi][0] - robot[ri+i])
            return best
        return go(0,0)