import numpy as np
import sympy
from fractions import Fraction as frac
def calculate_determinant(matrix):
        determinant = np.linalg.det(matrix)
        return determinant
    
def diagonal_transformation(matrix):
        x = sympy.symbols('x')
        #matrix = init_matrix(size_matrix,size_matrix)
        #sympy_matrix = sympy.Matrix(matrix)
        sympy_matrix = matrix
        diag = sympy_matrix.diagonal()
        for i in range(len(diag)):
            sympy_matrix[i,i] -=x
        det = sympy_matrix.det()
        solutions = sympy.solve(det, x)
       # print(solutions)
        size_matrix = matrix.shape[0]
        matrix_res = sympy.zeros(size_matrix,size_matrix)
        i=0
        my_đict = dict()
        for sol in solutions:
            real,image = sol.as_real_imag()
            if(real in my_đict):
                break
            else:
                my_đict[real] = image
                if image == 0:
                    matrix_res[i,i]=real
                    i+=1
                else:
                    matrix_res[i,i] = real
                    matrix_res[i,i+1] = image  
                    matrix_res[i+1,i]= -image
                    matrix_res[i+1,i+1]=real
                    i+=2
        matrix_res_list = matrix_res.tolist()
        return matrix_res_list
    



# hàm in ra kết quả dưới dạng hệ số là phân số thông qua limit_denominator======


def print_format_fraction(ortho_basis):
    m = len(ortho_basis)
    for row in range(m):
        for i, v in enumerate(ortho_basis[row]):
            print(
                f"v[{row}][{i}] = ({frac(v.real).limit_denominator(10)}) + ({frac(v.imag).limit_denominator(10)})j")


def gram_schmidt(vectors):
    n = len(vectors)
    ortho_vectors = []
    for i in range(n):
        u = vectors[i]
        for v in ortho_vectors:
            print(type(v[0]))
            if (type(v[0]) == 'numpy.complex128'):
                v_conjugate = v.conjugate()
            else:
                v_conjugate = v
            u -= np.dot(u, v) / np.dot(v, v_conjugate) * v
        ortho_vectors.append(u)
    # Convert the resulting vectors to complex with fractions
    return ortho_vectors


# =============== Dau vao la system vectors u and vector alpha============
def vector_projection(matrix):
    # u_1 = np.array([1+0j, 1+0j, 1, 1])
    # u_2 = np.array([1, 0+0j, 0, 3])
    # vec_alpha = np.array([4+0j, -1, -3, 4])
    # v3 = np.array([frac(2, 3) + frac(1, 4)*1j, frac(4, 5) - frac(3, 8)*1j])
    ortho_basis = gram_schmidt(matrix)

    # print_format_fraction(ortho_basis)
    # ========== result last vector of ortho_basis=========#
    projection_vector_alpha = ortho_basis[-1]
    result = "vector_alpha:\n"
    # result+=[f"({frac(x.real).limit_denominator(10)} + {frac(x.imag).limit_denominator(10)}j)"
    # for x in projection_vector_alpha]
    for x in projection_vector_alpha:
        result += f"({frac(x.real).limit_denominator(10)} + {frac(x.imag).limit_denominator(10)}j)   "
    return result



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