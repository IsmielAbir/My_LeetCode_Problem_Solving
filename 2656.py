class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        for i in range(mx+1, mx+k):
            mx+=i
        return mx

