class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        lengths = [1]
        limit = 0
        
        for op in operations:
            prev_len = lengths[-1]
            lengths.append(prev_len * 2)
            limit += 1
            if lengths[-1] >= k:
                break

        def trace(index, op_index):
            if op_index == 0:
                return 'a'
            prev_len = lengths[op_index - 1]
            if index < prev_len:
                return trace(index, op_index - 1)
            else:
                c = trace(index - prev_len, op_index - 1)
                if operations[op_index - 1] == 0:
                    return c
                else:
                    return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))

        return trace(k - 1, len(lengths) - 1)
        
        # TLE -> we are building string for k so fails for large k
        word= 'a'
        j = 0
        while len(word) < k:
            s = ''
            if operations[j] == 1:
                for i in word:
                    s += chr(ord(i) + 1)
            else:
                s += word
            word += s
            j += 1
        return word[k-1]