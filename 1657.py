class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c = Counter(word1)
        d = Counter(word2)
        a = sorted(c.values())
        b = sorted(d.values())
        return c.keys()==d.keys() and a==b
        