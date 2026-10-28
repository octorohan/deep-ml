def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    matrix_cpy = [row.copy() for row in matrix]  
    a = matrix_cpy[0][0]
    b = matrix_cpy[0][1]
    c = matrix_cpy[1][0]
    d = matrix_cpy[1][1]
    det = a*d - b*c
    if det == 0:
        return None
    a, d = d, a
    matrix_cpy[0][0] = a/det
    matrix_cpy[1][1] = d/det
    matrix_cpy[0][1] = -b/det
    matrix_cpy[1][0] = -c/det
    return matrix_cpy
    #pass