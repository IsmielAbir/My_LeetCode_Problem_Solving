class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for i in s:
            if i.isalnum():
                s1+=i
        p = s1.lower()
        if p==p[::-1]:
            return True
        else:
            return False
        