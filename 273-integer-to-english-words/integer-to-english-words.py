class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        # Dictionary for numbers 1 to 19
        ones_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }


        # Dictionary for tens from 20 to 90
        tens = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }


        # Dictionary for tens from 20 to 90
        tens = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        def get_str(n):
                res = []
                hundreds = n//100
                if hundreds:
                    res.append(ones_map[hundreds]+' Hundred')
                last_2 = n%100
                if last_2 >=20:
                    ten,ones = last_2//10,last_2%10
                    res.append(tens[ten*10])
                    if ones:
                        res.append(ones_map[ones])


                elif last_2:
                    res.append(ones_map[last_2])

                return " ".join(res)
        
        postfix = [""," Thousand"," Million"," Billion"]
        i=0
        res = []
        while num:
            digits = num%1000
            s = get_str(digits)
            if s:
                res = [s + postfix[i]]+res
            num = num//1000
            i+=1
        return " ".join(res)

            