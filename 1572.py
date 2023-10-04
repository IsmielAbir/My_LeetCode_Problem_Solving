class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j or i==len(mat)-j-1 or j==len(mat)-i-1:
                    sum+=mat[i][j]
        return sum
            
