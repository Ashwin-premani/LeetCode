class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n-1):
            count = 1
            temp = ''
            for i in range(1,len(s)):
                if s[i-1] == s[i]:
                    count += 1
                else:
                    temp += str(count) + s[i-1]
                    count = 1
            temp += str(count) + s[-1]
            s = temp
        return s






        s = '1'
        for _ in range(n - 1):
            temp = ''
            count = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    temp += str(count) + s[i - 1]
                    count = 1
            temp += str(count) + s[-1]
            s = temp
        return s
