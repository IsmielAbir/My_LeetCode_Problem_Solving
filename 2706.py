class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a = money-sum(sorted(prices)[:2])
        if a>=0:
            return a
        else:
            return money