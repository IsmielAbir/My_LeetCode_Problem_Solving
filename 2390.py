class Solution:
    def removeStars(self, s: str) -> str:
        li = []
        for i in s:
            if i != '*':
                li.append(i)
            else:
                li.pop()
        return ''.join(li)