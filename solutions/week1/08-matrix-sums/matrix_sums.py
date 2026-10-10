def matrix_sums(matrix):
    if not matrix:                           # empty matrix: matrix[0] below would crash
        return [], []
    row_sums = []
    col_sums = [0] * len(matrix[0])          # one running total per column, all starting at 0
    for row in matrix:
        total = 0
        for j, value in enumerate(row):      # j is the column index of this value
            total += value                   # builds this row's total
            col_sums[j] += value             # builds that column's total
        row_sums.append(total)
    return row_sums, col_sums


# shortcut once nested loops make sense: zip(*matrix) flips rows into columns
#     return [sum(row) for row in matrix], [sum(col) for col in zip(*matrix)]