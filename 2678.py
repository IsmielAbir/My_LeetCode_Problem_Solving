class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0
        for i in details:
            age_str = i[11:13]
            age = int(age_str)
            if age > 60:
                c += 1
        return c
