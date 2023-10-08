class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        e1 = []
        e2 = []
        odd1 = []
        odd2 = []

        for i in range(len(s2)):
            if i%2==0:
                e1.append(s1[i])
                e2.append(s2[i])
            else:
                odd1.append(s1[i])
                odd2.append(s2[i])
        return (sorted(e1)==sorted(e2) and sorted(odd1)==sorted(odd2))