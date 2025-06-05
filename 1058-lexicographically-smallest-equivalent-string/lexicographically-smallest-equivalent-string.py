class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Using union find near constant time per operation
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                if px < py:
                    parent[py] = px
                else:
                    parent[px] = py

        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))

        res = []
        for ch in baseStr:
            res.append(chr(find(ord(ch) - ord('a')) + ord('a')))

        return ''.join(res)


        # Straight Forward approach linear
        grp = []

        def find_group(ch):
            for g in grp:
                if ch in g:
                    return g
            return None

        for i in range(len(s1)):
            g1 = find_group(s1[i])
            g2 = find_group(s2[i])

            if g1 and g2:
                if g1 != g2:
                    g1.extend(g2)
                    grp.remove(g2)
            elif g1:
                g1.append(s2[i])
            elif g2:
                g2.append(s1[i])
            else:
                grp.append([s1[i], s2[i]])
        result = [sorted(set(g)) for g in grp]
        
        res = []
        for i in baseStr:
            found = False
            for sublist in result:
                if i in sublist:
                    res.append(sublist[0])
                    found = True
                    break
            if not found:
                res.append(i)
                
        return "".join(res)