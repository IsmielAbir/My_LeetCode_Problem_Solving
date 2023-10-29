class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        li = []
        for i in image:
            li.append([j^1 for j in i[::-1]])
        return li