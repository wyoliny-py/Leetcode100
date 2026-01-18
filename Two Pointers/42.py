# 42. Trapping Rain Water
class Solution:
    def trap(self, height: list[int]) -> int:
        l_wall, r_wall = 0, 0
        n = len(height)
        l_array = [0] * n
        r_array = [0] * n
        for i in range(n):
            j = -i - 1
            l_array[i] = l_wall
            r_array[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
        
        total = 0 
        for i in range(n):
            pot = min(l_array[i], r_array[i])
            total += max(0, pot - height[i])
        return total
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))