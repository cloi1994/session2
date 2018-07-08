class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or target is None: return False
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r-l)//2
            row, col = mid // n , mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
