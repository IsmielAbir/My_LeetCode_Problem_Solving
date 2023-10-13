class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        li = [words[0]]
        for i in range(1, len(words)):
            if sorted(words[i-1]) != sorted(words[i]):
                li.append(words[i])
        return li
