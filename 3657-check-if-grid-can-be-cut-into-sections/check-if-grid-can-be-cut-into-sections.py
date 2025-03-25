class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [(r[0], r[2]) for r in rectangles]
        y = [(r[1], r[3]) for r in rectangles]
        x.sort()
        y.sort()

        def count_nonoverlap(intervals):
            prev_end = -1
            reg = 0
            for s, e in intervals:
                if prev_end <= s:
                    reg += 1
                prev_end = max(prev_end, e)
            return reg
        return max(count_nonoverlap(x), count_nonoverlap(y)) >= 3

        # def can_cut(a, rectangles):
        #     rectangles.sort(key=lambda x: x[a])
        #     prev_a1 = -1
        #     prev_a2 = -1
        #     reg = 0
        #     for i in rectangles:
        #         if i[a] > prev_a1 and i[a+2] > prev_a2:
        #             reg += 1
        #         prev_a1 = max(prev_a1, i[a])
        #         prev_a2 = max(prev_a2, i[a+2])
        #     return reg >= 3

        # if can_cut(0, rectangles):
        #     return True
        # if can_cut(1, rectangles):
        #     return True
        # return False

        # def can_make_cuts(rectangles, index):
        #     rectangles.sort(key=lambda x: x[index])  
        #     prev_end = -1
        #     sections = 0
            
        #     for rect in rectangles:
        #         if rect[index] > prev_end: 
        #             sections += 1
        #             prev_end = rect[index + 2] 
        #     return sections >= 3
        # if can_make_cuts(rectangles, 0):
        #     return True
        # if can_make_cuts(rectangles, 1):
        #     return True
        # return False