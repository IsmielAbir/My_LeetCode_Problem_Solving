class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        m = 0
        for i in range(len(students)):
            m+= abs(students[i]-seats[i])
        return m
        