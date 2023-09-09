class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        c = 0
        h = 0
        for i in gain:
            c+= i
            h = max(c, h)
        return h
