class Solution:
    def integerBreak(self, n: int) -> int:
        if n <=3:
            return n-1

        num = n//3
        pro = 3**num

        if n%3==1:
            pro//=3
            pro*=4
        elif n%3==2:
            pro*=2
        return pro


        