class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if (event1[1]>=event2[0] and event1[0]<=event2[0]) or (event2[1]>=event1[0] and event2[0]<=event1[0]):
            return True
        return False