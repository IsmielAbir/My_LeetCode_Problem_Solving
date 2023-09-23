class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n+1)
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        elif dp[n]!=-1:
            return dp[n]
        else:
            dp[n] = self.fib(n-1) + self.fib(n-2)
            return dp[n]
        