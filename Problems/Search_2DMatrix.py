class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])

        l,r = 0, rows - 1

        while l <= r:
            row = (l + r)//2

            if target > matrix[row][-1]:
                l = row + 1
            elif target < matrix[row][0]:
                r = row - 1
            else:
                break
        
        row_c = matrix[row]

        l,r = 0, cols - 1

        while l <= r:
            m = (l + r)//2

            if row_c[m] < target:
                l = m + 1
            elif row_c[m] > target:
                r = m - 1
            else:
                return True
        
        return False