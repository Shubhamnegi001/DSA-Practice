class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        column = len(matrix[0])
        
        zero_row = set()
        zero_column = set()
        
        for i in range(rows):
            for j in range(column):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_column.add(j)
        
        for i in range(rows):
            for j in range(column):
                if i in zero_row or j in zero_column:
                    matrix[i][j] = 0
        
        for row in matrix:
            print(row)