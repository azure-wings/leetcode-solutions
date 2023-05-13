class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_begin, col_begin = 0, 0
        row_end, col_end = len(matrix) - 1, len(matrix[0]) - 1
        result = []

        while (row_begin <= row_end and col_begin <= col_end):
            for i in range(col_begin, col_end + 1):
                result.append(matrix[row_begin][i])
            row_begin += 1
            for i in range(row_begin, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1
            if row_begin <= row_end:
                for i in range(col_end, col_begin - 1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1
            if col_begin <= col_end:
                for i in range(row_end, row_begin - 1, -1):
                    result.append(matrix[i][col_begin])
                col_begin += 1

        return result