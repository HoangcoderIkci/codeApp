import fuldamentalsystem as fuld
import gram_chmidt
from sympy import factor, Symbol,Matrix
import sympy
def get_list_coefficients(expr,x):
    # x = sp.symbols('x')
    # expr = x**3 + x + 1
    degree = expr.as_poly().degree(x)
    coeffs_dict = expr.as_coefficients_dict()
    coeffs_list_result = []
    for i in range(degree+1):
        if x**i not in coeffs_dict:
            coeffs_list_result.append(0)
        else:
            coeffs_list_result.append(coeffs_dict[x**i])
    return(coeffs_list_result)


matrix_A = Matrix([[17,-8,4], 
                   [-8, 17,-4],
                   [4,-4,11]
                   ])
matrix_A *=1/2
matrix = sympy.Matrix(matrix_A)
x = sympy.symbols('x')
row,col = matrix.shape
t = min(row,col)
for i in range(t):
    matrix[i,i] -=x
#print("matrix: ", matrix)
det = matrix.det()
det = sympy.sympify(det)

# Khởi tạo biến

# Tạo một biểu thức
expr = det.copy()
#print("expr: ", expr)
# Phân tích biểu thức thành nhân tử
factored_expr = factor(expr)
#print("factored_expr: ", factored_expr)
# Lấy danh sách các nhân tử từ biểu thức đã phân tích
factors = factored_expr.as_ordered_factors()

print("factors: ", factors)
# list_result=[]
# for f in factors:
#     if f.as_poly.degree(x)!=0:
#         list_result.append(f)
system_basis_orth =[]
for f in factors:
        # print("type f: ", type(f))
        # if type(f) == 'sympy.core.numbers.NegativeOne':
        #     continue
        # print("polynomial",f)
        # if isinstance(f, sympy.core.numbers.NegativeOne):
        #     continue
        print("polynomial",f)
        poly_f = f.as_poly()
        if poly_f is None or poly_f.degree() == 0:
            continue
        coeffs = get_list_coefficients(f.expand(),x)
        matrix_result = matrix_A.copy()
        deg = 0
        for coeff in coeffs:
            #print("matrix_A",matrix_A)
            if coeff != 0:
                #temp = (matrix_A**deg) * coeff
                #print("temp",temp)
                matrix_result+=(matrix_A**(deg) )* coeff
            deg+=1 
        matrix_result -= matrix_A
        print("matrix_result_line65:",matrix_result)
        solution = fuld.solve_homogeneous_system(matrix_result.copy())
        print("solution",solution)
        gram_solution = gram_chmidt.gram_schmidt(solution)
        for sol in gram_solution:
            system_basis_orth.append(sol)
        i=0
        j=0
        for u_i in system_basis_orth:
            for u_j in system_basis_orth:
                #print(f"u[{i,j}]=",sympy.Matrix(u_i).dot(sympy.Matrix(u_j)))
                j+=1
            i+=1
        print("gram_solution",gram_solution)
print("system_basis_orth",system_basis_orth)
# In kết quả
