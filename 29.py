class Solution:
    def divide(self, d: int, di: int) -> int:
        a =  d/di
        if d == -2**31 and di == -1:
            return 2**31-1
        elif a>0:
            return floor(a)
        return ceil(a)