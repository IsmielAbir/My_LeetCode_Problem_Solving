class Solution:
    def calPoints(self, operations: List[str]) -> int:
        li = []
        for i in range(len(operations)):
            if operations[i].isdigit() or (operations[i][0] == '-' and operations[i][1:].isdigit()):
                li.append(int(operations[i]))
            elif operations[i] == '+':
                li.append(li[-1] + li[-2])
            elif operations[i] == 'D':
                li.append(2 * li[-1])
            elif operations[i] == 'C':
                li.pop()
        return sum(li)
