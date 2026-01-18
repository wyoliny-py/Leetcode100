# 682. Baseball Game
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stk = []
        for op in operations:
            print(stk)
            if op[-1] in '1234567890':
                stk.append(int(op))
            if op == '+':
                stk.append(stk[-1] + stk[-2])
            if op == 'D' and stk:
                stk.append(stk[-1] * 2)
            if op == 'C' and stk:
                stk.pop()
        return sum(stk)
print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))