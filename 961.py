class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        li = []
        for i in nums:
            if i in li:
                return i
            else:
                li.append(i)
