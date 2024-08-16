from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        change = {5: 0, 10: 0}
        

        for bill in bills:
            if bill == 5:

                change[5] += 1
            elif bill == 10:
               
                if change[5] > 0:
                    change[5] -= 1
                    change[10] += 1
                else:
                    return False
            elif bill == 20:
               
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False

        return True
