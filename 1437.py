class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c = k
        for i in nums:
            if i==1:
                if c<k:
                    return False
                c = 0
            else:
                c+=1
        return True