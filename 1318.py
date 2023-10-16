class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        x = (a|b) ^ c
        y = a & b & x
        return bin(x).count('1') + bin(y).count('1')
        