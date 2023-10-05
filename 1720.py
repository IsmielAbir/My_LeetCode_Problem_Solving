class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        li = []
        li.append(first)
        for i in encoded:
            temp = i^first
            li.append(temp)
            first = temp
        return li
            