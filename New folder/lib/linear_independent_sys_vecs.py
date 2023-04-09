import numpy as np
def find_system_linearly_independent_vectors(systems_vectors):
    
# Define the system vectors
# v1 = np.array([1, 2, 3])
# v2 = np.array([4, 8, 12])
# v3 = np.array([1, 2, 3])

# Create a matrix from the system vectors
    A = np.array(systems_vectors)
# Perform row-reduction on the matrix
    B = A.copy().astype(np.float64)
    B = B.T
    pivots = []
    for i in range(len(B[0])):
        row = len(pivots)
        while row < len(B) and B[row, i] == 0:
            row += 1
        if row == len(B):
            continue
        pivots.append(i)
        if row != len(pivots) - 1:
            B[[row, len(pivots) - 1], :] = B[[len(pivots) - 1, row], :]
        for j in range(row + 1, len(B)):
            B[j, :] -= B[j, i] / B[len(pivots) - 1, i] * B[len(pivots) - 1, :]
    # Identify the linearly independent vectors
    lin_ind_vectors = A.T[:, pivots]
    # Print the linearly independent vectors
    result ="The linearly independent vectors are:\n"
    for vector in lin_ind_vectors.T:
        result+=f"{vector}\n"
    return result
