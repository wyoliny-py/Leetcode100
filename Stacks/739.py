# 739. Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # O(n^2), Time Limit
        # n = len(temperatures)
        # answer = []
        # for i in range(n):
        #     j = i + 1
        #     flag = False
        #     while j < n:
        #         if temperatures[j] > temperatures[i]:
        #             flag = True
        #             break
        #         else:
        #             j += 1
        #     if flag:
        #         answer.append(j - i)
        #     else:
        #         answer.append(0)
        # return answer


        n = len(temperatures)
        answer = [0] * n
        stk = []
        for i in range(n):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                stk_i = stk.pop()
                answer[stk_i] = i - stk_i
            stk.append(i)
        return answer  # O(n)
print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73])) 