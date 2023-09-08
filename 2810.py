class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = ''
        for i in s:
            if i  == 'i':
                a = a[::-1]
            else:
                a = a+ i
        return a
