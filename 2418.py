class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        li = []
        for i in range(len(names)):
            li.append([heights[i], names[i]])
        li = sorted(li, reverse=True)
        return [name for height, name in li]
        