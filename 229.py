class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        li = []
        for i in set(nums):
            if nums.count(i) > len(nums)//3:
                li.append(i)
        return li
        