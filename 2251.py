class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        starts = []
        ends = []

        for i,j in flowers:
            starts.append(i)
            ends.append(j+1)

        starts.sort()
        ends.sort()
        ans = []

        for p in people:
            n = bisect_right(starts, p)
            m = bisect_right(ends, p)
            ans.append(n-m)
        
        return ans


