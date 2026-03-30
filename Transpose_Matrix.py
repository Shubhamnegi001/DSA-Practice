class Solution:
    def transpose(self, matrix):
        rows = len(matrix)
        column = len(matrix[0])
        transpose = [[0]*rows for _ in range(column)]
        for i in range(rows):
            for j in range(column):
                transpose[j][i] = matrix[i][j]
        return transpose