class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        dic = {}
        for i in a:
            dic[i[-1]] = i[:-1]
        return ' '.join([dic[j] for j in sorted(dic)])
