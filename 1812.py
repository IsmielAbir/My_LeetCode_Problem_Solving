class Solution:
    def squareIsWhite(self, c: str) -> bool:
        return (ord(c[0])+ord(c[1])) & 1
