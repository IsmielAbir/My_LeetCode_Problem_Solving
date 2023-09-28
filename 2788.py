class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        li = []
        for i in words:
            for j in i.split(separator):
                if j:
                    li.append(j)

        return li