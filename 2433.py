class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        li = [pref[0]]
        for i in range(len(pref)-1):
            li.append(pref[i]^pref[i+1])
        return li