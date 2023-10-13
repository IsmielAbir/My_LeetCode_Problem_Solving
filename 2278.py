class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        ss = len(s)
        c = 0
        for i in s:
            if i in letter:
                c+=1
        return int((c/ss)*100)