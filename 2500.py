class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        c = 0
        for i in range(len(grid[0])):
            m  = 0
            for j in grid:
                n = max(j)
                m = max(n, m)
                j.remove(n)
            c+=m
        return c
