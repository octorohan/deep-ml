def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    
    n1 = len(a) #rows
    n2 = len(a[0]) #column
    transpose = [[0] * n1 for _ in range(n2)]
    
    for i in range(n1):
        for j in range(n2):
            transpose[j][i] = a[i][j]
    return transpose
    #pass