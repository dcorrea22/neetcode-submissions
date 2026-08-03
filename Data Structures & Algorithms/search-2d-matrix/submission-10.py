class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        i = 0
        j = len(matrix) - 1

        while i <= j:
            mid = (i + j) // 2
            if matrix[mid][0] < target:
                i = mid + 1
            elif matrix[mid][0] > target:
                j = mid - 1
            else:
                return True
        t = min(i, j)
        if matrix[t][0] > target:
            t = max(0, t - 1)
        
        print(t)
        i = 0
        j = len(matrix[t]) - 1
        
        while i <= j:
            mid = (i+j) // 2

            if matrix[t][mid] < target:
                i = max(mid + 1, i+1)
            elif matrix[t][mid] > target:
                j = min(mid - 1, j-1)
            else:
                return True

        return False
        

        