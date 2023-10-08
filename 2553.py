class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        li = []
        for i in nums:
            s = str(i)
            for j in s:
                li.append(int(j))
        return li
        