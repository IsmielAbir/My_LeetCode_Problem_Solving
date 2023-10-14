class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1
    
        while factor <= n:
            div = factor * 10
            count += (n // div) * factor + min(max(n % div - factor + 1, 0), factor)
            factor *= 10
    
        return count