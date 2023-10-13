class Solution:
    def largestGoodInteger(self, num: str) -> str:
        li = ["000","111","222","333","444","555","666","777","888","999"]
        lst = []
        for i in li:
            if i in num:
                lst.append(i)
        lst.sort()
        if len(lst)>0:
            return lst[-1]
        else:
            return ""
                