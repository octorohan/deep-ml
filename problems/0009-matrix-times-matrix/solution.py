def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    n1 = len(a) #rows
    n2 = len(a[0]) #column
    n3 = len(b) #rows
    n4 = len(b[0]) #column
    if n2 != n3:
        return -1 
    c = [[0]* n4 for _ in range(n1)]

    for i in range(n1):
        for j in range(n4):
            for k in range(n2):
                c[i][j] += a[i][k]*b[k][j]
    return c