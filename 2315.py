class Solution:
    def countAsterisks(self, s: str) -> int:
        c  = 0 
        f = False
        for i in s:
            if i=='|':
                f = not(f)
            if i=='*' and f == False:
                c+=1
        return c