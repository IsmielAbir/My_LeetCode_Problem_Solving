class Solution:
    def alternateDigitSum(self, n: int) -> int:
        a = 0
        n = str(n)
        for i in range(len(n)):
            if i%2==0:
                a+=int(n[i])
            else:
                a-=int(n[i])
        return a
