class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        r = 0
        p1 = 0
        p2 = len(nums)-1

        while p1<=p2:

            if p1==p2:
                r += int(nums[p1])
            else:
                r+=int(str(nums[p1])+str(nums[p2]))

            p1+=1
            p2-=1
        
        return r
