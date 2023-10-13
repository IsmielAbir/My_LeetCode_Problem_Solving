class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        c = columnNumber
        r = ''
        while c:
            c-=1
            s = c%26
            c//=26
            r = chr(65+s)+r
        return r
        