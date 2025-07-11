class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        lowercase = set(string.ascii_lowercase)
        uppercase = set(string.ascii_uppercase)
        digits = set(str(e) for e in range(10)) 

        deletion = max(0, len(password) - 20)
        lower = any(c in lowercase for c in password)
        upper = any(c in uppercase for c in password)
        digit = any(c in digits for c in password)
        missing = (not lower) + (not upper) + (not digit)


        def count_len(s):
            res = [1]
            last = s[0]
            for i in range(1, len(s)):
                if s[i] == last:
                    res[-1] += 1
                else:
                    res.append(1)
                last = s[i]
            return res
        
        sub_len = count_len(password) 
        
        def break_sub(sub_len, deletion):
            while deletion > 0:
                best_tuple = min(enumerate(sub_len), key = lambda pair: pair[1] % 3 if pair[1] >= 3 else float('inf'))
                best_idx = best_tuple[0]
                sub_len[best_idx] -= 1
                deletion -= 1
        break_sub(sub_len, deletion)

        breaks = sum(length // 3 for length in sub_len if length >= 3)
        insertion = max(0, 6-len(password))
        return deletion + max(missing, breaks, insertion)

        # Failed
        res = 0
        lower = 0
        upper = 0
        digit = 0
        count = 1
        repeat_replacements = 0
        prev = ''
        for i in range(len(password)):
            c = password[i]  
            if c == prev:
                count += 1
                if count == 3:
                    repeat_replacements += 1  
                    count = 1  
            else:
                count = 1
            prev = c

            if c.islower():
                lower = 1
            elif c.isupper():
                upper = 1
            elif c.isdigit():
                digit = 1

        missing_types = 3 - (lower + upper + digit)

        if len(password) < 6:
            return max(6 - len(password), missing_types)
        elif len(password) <= 20:
            return max(missing_types, repeat_replacements)
        else:
            delete_needed = len(password) - 20
            repeat_replacements = max(repeat_replacements - delete_needed, 0)
            return delete_needed + max(missing_types, repeat_replacements)