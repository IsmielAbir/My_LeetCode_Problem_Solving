class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        li = [[]]
        for i in nums:
            li += [j + [i] for j in li]
        return li
