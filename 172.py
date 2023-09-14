class Solution:
    def trailingZeroes(self, n: int) -> int:
        c = 0
        if n<5:
            return 0
        while n>=5:
            c += int(n/5)
            n = int(n/5)
        return c
        