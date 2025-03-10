class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def atleastk(k):
            vowel = defaultdict(int)
            n = 0
            res = 0
            l = 0
            for r in range(len(word)):
                if word[r] in 'aeiou':
                    vowel[word[r]] += 1
                else:
                    n += 1
                while len(vowel) == 5 and n >= k:
                    res += (len(word) - r)
                    if word[l] in 'aeiou':
                        vowel[word[l]] -= 1
                    else:
                        n -= 1
                    if vowel[word[l]] == 0:
                        vowel.pop(word[l])
                    l += 1

            return res
        
        return atleastk(k) - atleastk(k+1)
        
        
        
        # vowels = {'a', 'e', 'i', 'o', 'u'}
        # result = 0
        
        # for i in range(len(word)):
        #     vowel_set = set()
        #     consonant_count = 0
            
        #     for j in range(i, len(word)):
        #         if word[j] in vowels:
        #             vowel_set.add(word[j])
        #         else:
        #             consonant_count += 1
                
        #         if len(vowel_set) == 5 and consonant_count == k:
        #             result += 1
                
        #         if consonant_count > k:
        #             break
            
        # return result