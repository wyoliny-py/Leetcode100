# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        flaging = {1: True, 2: False, 3: False, 4: False}
        n = len(matrix)
        m = len(matrix[0])
        ans_list = []
        i = 0
        j = 0
        visited = [[False] * m for _ in range(n)]
        while len(ans_list) < n * m:
            if flaging[1]:  # Движение вправо
                while j < m and not visited[i][j]:
                    ans_list.append(matrix[i][j])
                    visited[i][j] = True
                    j += 1
                j -= 1
                i += 1
                flaging[1] = False
                flaging[2] = True
                
            elif flaging[2]:
                while i < n and not visited[i][j]:
                    ans_list.append(matrix[i][j])
                    visited[i][j] = True
                    i += 1
                i -= 1
                j -= 1
                flaging[2] = False
                flaging[3] = True
                
            elif flaging[3]:
                while j >= 0 and not visited[i][j]:
                    ans_list.append(matrix[i][j])
                    visited[i][j] = True
                    j -= 1
                j += 1
                i -= 1
                flaging[3] = False
                flaging[4] = True
                
            elif flaging[4]:
                while i >= 0 and not visited[i][j]:
                    ans_list.append(matrix[i][j])
                    visited[i][j] = True
                    i -= 1
                i += 1
                j += 1
                flaging[4] = False
                flaging[1] = True
        
        return ans_list