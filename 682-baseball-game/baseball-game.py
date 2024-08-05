class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        notint=["C","D","+"]
        for i in operations:
            if i not in notint:
                score.append(int(i))
            else:
                if i=="C":
                    score.pop()
                elif i=="D":
                    score.append(2*score[len(score)-1])
                else:
                    score.append((score[len(score)-1])+(score[len(score)-2]))
        return sum(score)