class Solution:
    def isFascinating(self, n: int) -> bool:
        d = str(n)+str(n*2)+str(n*3)
        if '0' in d:
            return False
        if len(d)>9:
            return False
        for i in range(1,10):
            if str(i) not in d:
                return False
        return True

     