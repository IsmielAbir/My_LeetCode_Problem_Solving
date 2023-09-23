class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(u):
            li = []
            for i in u:
                if i != '#':
                    li.append(i)
                elif li:
                    li.pop()
            return "".join(li)
        return build(s) == build(t)