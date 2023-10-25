class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        c = bin(k-1).count('1')
        return 0 if c%2==0 else 1