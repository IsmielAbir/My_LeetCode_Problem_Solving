class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        li = [1]
        prev = 1
        for i in range(1, rowIndex+1):
            n = prev * (rowIndex-i+1)//i
            li.append(n)
            prev = n
        return li
        