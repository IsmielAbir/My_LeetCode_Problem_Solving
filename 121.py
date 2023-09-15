class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        mx = 0
        for i in prices[1:]:
            mx = max(mx, i-mn)
            mn = min(mn, i)
        return mx
