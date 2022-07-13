def zero_matrix(matrix):
    m, n = len(matrix), len(matrix[0])
    rows = set()
    cols = set()

    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                rows.add(r)
                cols.add(c)

    for r in range(m):
        for c in range(n):
            if (r in rows) or (y in cols):
                matrix[r][c] = 0

    return matrix