class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a = ''
        for i in range(len(s)):
            a+=s[indices.index(i)]
        return a
