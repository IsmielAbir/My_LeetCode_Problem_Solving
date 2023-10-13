from datetime import datetime

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def get_date(d):
            return datetime.strptime(d, '%m-%d')
        return max(0, (min(get_date(leaveAlice), get_date(leaveBob)) - max(get_date(arriveAlice), get_date(arriveBob))).days + 1)