class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = list(str(x))
        if a == a[::-1]:
            return True
        else:
            return False