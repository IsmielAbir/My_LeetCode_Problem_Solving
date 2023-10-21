class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        li = []
        for i in s:
            li.append(s.count(i))
        if len(set(li))==1:
            return True
        else:
            return False
        
        