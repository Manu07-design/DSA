class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows*cols - 1
        while l <= r:
            mid = (l+r)//2
            row = mid//cols
            col = mid % cols
            value = matrix[row][col]
            if value == target:
                return True
            elif value < target:
                l = mid + 1
            else:
                r = mid - 1
        return False