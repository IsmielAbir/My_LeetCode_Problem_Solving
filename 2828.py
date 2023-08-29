class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ans = ""
        for word in words:
            ans+=word[0]
        return ans==s