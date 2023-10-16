class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<r:
            mid = (l+r)//2

            h_n = sum((p+ mid-1) // mid for p in piles)

            if h_n<=h:
                r = mid
            else:
                l = mid+1
        
        return l
        