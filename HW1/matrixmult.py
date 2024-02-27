def split_matrix(matrix):
    
    n = len(matrix)
    mid = n // 2
    A = [row[:mid] for row in matrix[:mid]]
    B = [row[mid:] for row in matrix[:mid]]
    C = [row[:mid] for row in matrix[mid:]]
    D = [row[mid:] for row in matrix[mid:]]
    return A, B, C, D

def add_matrices(matrix1, matrix2):
    
    n = len(matrix1)
    return [[matrix1[i][j] + matrix2[i][j] for j in range(n)] for i in range(n)]

def subtract_matrices(matrix1, matrix2):
    n1 = len(matrix1)
    n2 = len(matrix2)
    m1 = len(matrix1[0])
    m2 = len(matrix2[0])
    
    if n1 != n2 or m1 != m2:
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    
    return [[matrix1[i][j] - matrix2[i][j] for j in range(m1)] for i in range(n1)]


def strassen(n, m, p, matrix1, matrix2):
    """
    Strassen algorithm for matrix multiplication.
    """
    if n == 1 and m == 1 and p == 1:
        return [[matrix1[0][0] * matrix2[0][0]]]

    elif n == 1 and m == 1:
        return [[matrix1[0][0] * matrix2[i][0]] for i in range(p)]

    elif m == 1 and p == 1:
        return [[matrix1[i][0] * matrix2[0][0]] for i in range(n)]

    else:
        A, B, C, D = split_matrix(matrix1)
        E, F, G, H = split_matrix(matrix2)

        # recursively compute the seven matrix products
        P1 = strassen(n//2, m//2, p//2, A, subtract_matrices(F, H))
        P2 = strassen(n//2, m//2, p//2, add_matrices(A, B), H)
        P3 = strassen(n//2, m//2, p//2, add_matrices(C, D), E)
        P4 = strassen(n//2, m//2, p//2, D, subtract_matrices(G, E))
        P5 = strassen(n//2, m//2, p//2, add_matrices(A, D), add_matrices(E, H))
        P6 = strassen(n//2, m//2, p//2, subtract_matrices(B, D), add_matrices(G, H))
        P7 = strassen(n//2, m//2, p//2, subtract_matrices(A, C), add_matrices(E, F))

        # return the addition of the 7-products
        top_left = add_matrices(subtract_matrices(add_matrices(P5, P4), P2), P6)
        top_right = add_matrices(P1, P2)
        bottom_left = add_matrices(P3, P4)
        bottom_right = subtract_matrices(subtract_matrices(add_matrices(P1, P5), P3), P7)

        Z = [[0 for _ in range(p)] for _ in range(n)]
        for i in range(n//2):
            for j in range(p//2):
                Z[i][j] = top_left[i][j]
                Z[i][j + p//2] = top_right[i][j]
                Z[i + n//2][j] = bottom_left[i][j]
                Z[i + n//2][j + p//2] = bottom_right[i][j]

        return Z

def main():
    n1, m1 = map(int, input("Enter the size of matrix A (rows, columns): ").split(','))
    n2, m2 = map(int, input("Enter the size of matrix B (rows, columns): ").split(','))

    print("Enter the elements of matrix A row-wise and separated by commas:")
    matrix1 = [[int(x) for x in input().split(',')] for _ in range(n1)]

    print("Enter the elements of matrix B row-wise and separated by commas:")
    matrix2 = [[int(x) for x in input().split(',')] for _ in range(n2)]

    if m1 != n2:
        print("Error: The number of columns in matrix A must be equal to the number of rows in matrix B.")
        return

    result = strassen(n1, m1, m2, matrix1, matrix2)
    print("Z:")
    for row in result:
        print(row)

if __name__ == "__main__":
    main()
