class Solution:
    def countBits(self, n: int) -> List[int]:
        li = []
        a = 0
        for i in range(n+1):
            a = bin(i).count('1')
            li.append(a)
        return li
            