# 56. Merge Intervals
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        ans_matrix = []
        x = intervals[0]
        for i in range(1, len(intervals)):
            if x[1] >= intervals[i][0]:
                x = [x[0], max(x[1], intervals[i][1])]
            else:
                ans_matrix.append(x)
                x = intervals[i]
        ans_matrix.append(x)
        return ans_matrix
    
        # Time: O(n log n)
	    # Space: O(n)