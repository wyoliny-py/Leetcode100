# 150. Evaluate Reverse Polish Notation (RPN)
from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stk = []
        for char in tokens:
            if char in '+-*/':
                new_last = stk.pop()
                new_predlast = stk.pop()
                if char == '+':
                    stk.append(new_last + new_predlast)
                elif char == '-':
                    stk.append(new_predlast - new_last)
                elif char == '*':
                    stk.append(new_last * new_predlast)
                elif char == '/':
                    division = new_predlast / new_last
                        
                    if division < 0:
	                    stk.append(ceil(division))
                    else:
                        stk.append(floor(division))
            else:
                stk.append(int(char))
                    
        return stk[0]
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))