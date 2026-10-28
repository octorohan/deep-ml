import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	#n1 = a[0].len()
	#n2 = b.len()
	#if n1 != n2:
	#	return -1 
	#c: list(n1)
	#for i in range(n1):
	#	c[i] = 
	#pass

    if len(a[0]) != len(b):
        return -1

    return np.dot(a, b).tolist()	