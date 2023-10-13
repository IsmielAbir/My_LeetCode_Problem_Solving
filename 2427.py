class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c = 0
        d = gcd(a,b)
        for i in range(1,d+1):
            if d%i==0:
                c+=1
        return c