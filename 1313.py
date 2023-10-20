class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        li = []
        for i in range(0, len(nums), 2):
            v = nums[i+1]
            li+=([v]*nums[i])
        return li
        