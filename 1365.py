class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ls = []
        for i in range(len(nums)):
            c = 0
            for j in range(len(nums)):
                if(j!= i and nums[j]< nums[i]):
                    c+=1
            ls.append(c)
        return ls
