class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def func(i, s, path, res):
            if i == len(s):
                res.append(path.copy())
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    path.append(s[i:j+1])
                    func(j+1, s, path, res)
                    path.pop(len(path) - 1)
            
        res = []
        path = []
        func(0, s, path, res)
        return res
