
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


matrix_A = Matrix([[2,-1 ,2], 
                   [2, 2,-1],
                   [-1,2,2]
                   ])
matrix_A *=1/3
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