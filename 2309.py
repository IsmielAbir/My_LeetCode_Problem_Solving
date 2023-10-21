class Solution:
    def greatestLetter(self, s: str) -> str:
        c = 0
        for i in set(s):
            if i.isupper() and i.lower() in s:
                c = max(c, ord(i))
        if c == 0:
            return ""
        return chr(c)
