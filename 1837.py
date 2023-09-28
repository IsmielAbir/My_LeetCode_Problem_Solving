class Solution:
    def sumBase(self, n: int, k: int) -> int:
        a = 0
        while n!=0:
            if n//k:
                a+=n%k
                n//=k
            else:
                a+=n
                n=0
        return a