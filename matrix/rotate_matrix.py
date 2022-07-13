from locale import MON_12


def rotate_matrix(m):
    n = len(m)

    for layer in range(n // 2):
        start, end = layer, n - layer - 1
        for i in range(start, end):
            temp = m[layer][i]
            m[layer][i] = m[n - i - 1][layer]
            m[n - i - 1][layer] = m[n - layer - 1][n - i - 1]
            m[n - layer -1][n - i - 1] = m[i][n - layer - 1] 
            m[i][n - layer - 1] = temp
        
    return m

def rotate_matrix_swap(m):
    # n = len(m)

    def transpose(m):
        n = len(m)
        for row in range(n - 1):
            for col in range(row + 1, n):
                m[row][col], m[col][row] = m[col][row], m[row][col]
        return m
    
    def reflect(m):
        n = len(m)
        for r in range(n):
            for c in range(n // 2):
                m[r][c], m[r][n - c - 1] = m[r][n - c - 1], m[r][c]
        return m

    tran_m = transpose(m)
    ref_m = reflect(tran_m)

    return ref_m
    


if __name__ == '__main__':
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
    # for m1, expected in test_cases:
    #     r1 = rotate_matrix(m1)
    #     # print(r1)
    #     print(r1 == expected)
    
    for m2, expected in test_cases:
        r2 = rotate_matrix_swap(m2)
        print(r2)
        print(r2 == expected)
    