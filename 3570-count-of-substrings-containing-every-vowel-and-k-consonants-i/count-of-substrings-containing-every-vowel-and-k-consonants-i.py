class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = 0
        
        # Find all possible substrings
        for i in range(len(word)):
            vowel_set = set()
            consonant_count = 0
            
            for j in range(i, len(word)):
                # Process current character
                if word[j] in vowels:
                    vowel_set.add(word[j])
                else:
                    consonant_count += 1
                
                # Check if current substring has all vowels and exactly k consonants
                if len(vowel_set) == 5 and consonant_count == k:
                    result += 1
                
                # If we exceed k consonants, no need to continue this window
                if consonant_count > k:
                    break
            
        return result
