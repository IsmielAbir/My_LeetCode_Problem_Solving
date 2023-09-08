class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        a=0
        for i in range(0, len(hours)):
            if hours[i]>= target:
                a = a+1
        return a