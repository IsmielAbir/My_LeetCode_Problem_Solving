class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        s = set(word1+word2)
        for i in s:
            r = abs(word1.count(i)-word2.count(i))>=4
            if r:
                return False
        return True