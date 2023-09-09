from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = nums[0]
        maxi = nums[0]
        for i in nums:
            if i>maxi:
                maxi = i
            elif i<mini:
                mini = i
        return gcd(mini, maxi)