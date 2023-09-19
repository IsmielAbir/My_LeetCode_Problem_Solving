class Solution:
    def reverseBits(self, n: int) -> int:
        a = (bin(n)[2:])
        if len(a)<32:
            a = '0'*(32-len(a))+a
        return int(a[::-1],2)
