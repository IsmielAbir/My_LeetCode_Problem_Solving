class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        r = []
        for i in range(n):
            r.append(nums[i])
            r.append(nums[i+n])
        return r