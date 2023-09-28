class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        li = []
        lb = []
        for i in nums:
            if i%2==0:
                li.append(i)
            else:
                lb.append(i)
        return li+lb
            