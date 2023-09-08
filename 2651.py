class Solution:
    def findDelayedArrivalTime(self, a: int, d: int) -> int:
        if a+d<24:
            return a+d
        else:
            return (a+d)-24
        