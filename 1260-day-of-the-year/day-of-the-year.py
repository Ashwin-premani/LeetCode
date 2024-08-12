class Solution:
    def dayOfYear(self, date: str) -> int:
        def leap(year):
            if year%4==0:
                if year%100==0:
                    if year%400==0:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
    
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if leap(year):
            days_in_month[1] = 29
        
        days = 0
        for i in range(month - 1):
            days += days_in_month[i]
        
        days += day
        
        return days
            