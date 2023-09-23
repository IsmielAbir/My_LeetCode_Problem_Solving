class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0  
        
        for a, b, c, d in combinations(nums, 4):
            if a + b + c == d:
                count += 1
                
        return count