class Solution:
    def pivotInteger(self, n: int) -> int:
        l = 0
        r = 0
        for i in range(1, n+1):
            l = sum(range(1, i+1))
            r = sum(range(i, n+1))
            if l==r:
                return i
        return -1