class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        li = []
        for i in set(arr):
            li.append(arr.count(i))
        return len(set(li)) == len(set(arr))