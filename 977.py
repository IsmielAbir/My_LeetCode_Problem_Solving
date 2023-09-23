class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        li = []
        for i in nums:
            li.append(i*i)
        li.sort()
        return li
        