# 74. Search a 2D Matrix
def binary_search(arr, target):
    left, right = 0, len(arr) - 1  
    while left <= right:
        mid = left + (right - left) // 2  
        if arr[mid] == target:
            return True
        elif arr[mid] < target: 
            left = mid + 1  
        else: 
            right = mid - 1  
    return False
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if binary_search(matrix[i], target):
                return True
        return False