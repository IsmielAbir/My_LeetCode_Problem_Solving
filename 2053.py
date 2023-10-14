class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        li = []
        for i in arr:
            if arr.count(i)==1:
                li.append(i)
            
        if len(li)<k:
            return ""
        return li[k-1]
        