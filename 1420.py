class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9+7
        @lru_cache(None)
        def dp(i, h,k):
            if i==n and k==0:
                return 1
            if i==n or k<0:
                return 0
            return sum(dp(i+1, max(h,j), k-(j>h)) for j in range(1,m+1))%mod
        return dp(0,-1,k)
        