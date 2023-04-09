import tkinter as tk
import numpy as np
import sympy
from fractions import Fraction
from lib import lib_matrix
from lib import linear_independent_sys_vecs


root = tk.Tk()
root.title("Matrix Beta by Hoang-Ikci")

# Create matrix entries
matrix_entries = []
num_rows = 0
num_cols = 0
def create_matrix():
    # Clear previous matrix entries
    for row in matrix_entries:
        for entry in row:
            entry.destroy()
    matrix_entries.clear()

    # Get number of rows and columns
    num_rows = entry1.get()
    num_cols = entry2.get()
    #print(num_cols,num_rows)
    # Check if input fields are not empty
    if num_rows and num_cols:
        num_rows = int(num_rows)
        num_cols = int(num_cols)
        for i in range(num_rows):
            row = []
            for j in range(num_cols):
                entry = tk.Entry(root)
                entry.grid(row=i+5, column=j)
                row.append(entry)
            matrix_entries.append(row)
            #print("called, matrix entries:",matrix_entries)
    else:
        tk.messagebox.showerror(title="Error", message="Please enter the number of rows and columns.")
        
def init_matrix(n=num_rows,m=num_cols):
    matrix_results = []
    for row in matrix_entries:
            temp=[]
            for entry in row:
                user_input = entry.get().strip()  # Lấy chuỗi nhập vào và xóa khoảng trắng thừa
                if user_input:
                # Tách chuỗi thành phần thực và phần ảo
                    if '+' in user_input:
                        real_str, imag_str = user_input.split('+')
                    else:
                        real_str = user_input
                        imag_str = '0'
                # Chuyển đổi các phần tử thành phân số
                    real_fraction = Fraction(real_str.strip())
                    imag_fraction = Fraction(imag_str.strip().replace('j', ''))
                # Tạo số phức từ phần thực và phần ảo
                    complex_number = complex(real_fraction, imag_fraction)
                    temp.append(complex_number)
                else:
                    temp.append(complex(0))
            matrix_results.append(temp)
    return matrix_results
            

    
def format_matrix_output(matrix_res_list):
    text_result = ""
    for row in matrix_res_list:
            for element in row:
                #print(element, end=' ')
                text_result+= '{0:.{1}f}'.format(element,2) + '  '
            text_result += '\n'
    return text_result
            
is_transformating = False
def diagonal_transformation():
    global is_transformating
    if is_transformating:
        print("Transformating matrix,please wait....")
        return
    is_transformating = True
    try:
        #matrix = sympy.Matrix([[float(entry.get()) for entry in row] for row in matrix_entries])
        matrix=sympy.Matrix(init_matrix())
        # Check if matrix has at least two rows and two columns
        if matrix.shape[0] < 2 or matrix.shape[1] < 2:
            raise ValueError
        #size_matrix = 2
        x = sympy.symbols('x')
        #matrix = init_matrix(size_matrix,size_matrix)
        #sympy_matrix = sympy.Matrix(matrix)
        sympy_matrix = matrix
        diag = sympy_matrix.diagonal()
        for i in range(len(diag)):
            sympy_matrix[i,i] -=x
        det = sympy_matrix.det()
        print("det: ",det)
        solutions = sympy.solve(det, x)
        print(solutions)
        size_matrix = len(matrix_entries)
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
        text_result=format_matrix_output(matrix_res_list)
        result_label_transformation.config(text=text_result)
    except ValueError:
        # Show error message if input is invalid
        result_label_transformation.config(text="Invalid input")

    finally:
        print("tinh xong")
        is_transformating= False

is_loading_inverse_transform = False    
def inverse_transform():
    global is_loading_inverse_transform
    if is_loading_inverse_transform:
        print("finding please wait...")
        return
    is_loading_inverse_transform = True
    print("finding inverse butted") # Kiểm tra xem hàm này có được gọi đến hay không
    try:
        # Convert entries to numpy array
        #matrix = np.array([[complex(entry.get()) for entry in row] for row in matrix_entries])
        matrix=np.array(init_matrix())
        #print("Calculating determinant , matrix_entries:",matrix_entries)
        # Check if matrix has at least two rows and two columns
        if matrix.shape[0] < 2 or matrix.shape[1] < 2:
            raise ValueError
        # Calculate determinant
        inverse_matrix = np.linalg.inv(matrix)
        # Show result
        result_label_inverse_matrix.config(text=f"Inverse: {inverse_matrix}")

    except ValueError:
        # Show error message ifis_calculating input is invalid
        result_label_inverse_matrix.config(text="Invalid input")

    finally:
        print("tinh xong")
        is_loading_inverse_transform = False
    
    
    
is_finding_det_matrix = False

def calculate_determinant():
    
    global is_finding_det_matrix
    if is_finding_det_matrix:
        print("Calculating determinant please wait...")
        return
    is_finding_det_matrix = True
    print("Calculate determinant button pressed") # Kiểm tra xem hàm này có được gọi đến hay không
    try:
        # Convert entries to numpy array
        #matrix = np.array([[complex(entry.get()) for entry in row] for row in matrix_entries])
        matrix=np.array(init_matrix())
        #print("Calculating determinant , matrix_entries:",matrix_entries)
        # Check if matrix has at least two rows and two columns
        if matrix.shape[0] < 2 or matrix.shape[1] < 2:
            raise ValueError
        # Calculate determinant
        determinant = np.linalg.det(matrix)
        print("determinant: ", determinant)
        # Show resultis_finding det_matrix
        result_label.config(text=f"Determinant: {determinant:.3f}")

    except ValueError:
        # Show error message if input is invalid
        result_label.config(text="Invalid input")

    finally:
        is_finding_det_matrix = False

is_loading_systems_linear = False

def linear_independent_sys_vecs():
    
    global is_loading_systems_linear
    if is_loading_systems_linear:
        print("finding linea please wait...")
        return
    is_loading_systems_linear = True
    print("finding linear_independent_sys_vecs button pressed") # Kiểm tra xem hàm này có được gọi đến hay không
    try:

        matrix=np.array(init_matrix())
        system_linear_independent = lib_matrix.find_system_linearly_independent_vectors(matrix)

        # Show result
        result_label_linear_systems.config(text=system_linear_independent)

    except ValueError:
        # Show error message if input is invalid
        result_label_linear_systems.config(text="Invalid input")

    finally:
        is_loading_systems_linear = False


is_transformating_special_step_matrix = False
def transform_special_step_matrix():
    global is_transformating_special_step_matrix
    if is_transformating_special_step_matrix:
        print("Transformating matrix special,please wait....")
        return
    is_transformating_special_step_matrix = True
    try:
        matrix = np.array(init_matrix())
        #matrix = np.array([[float(entry.get()) for entry in row] for row in matrix_entries])
        # Check if matrix has at least two rows and two columns
        if matrix.shape[0] < 2 or matrix.shape[1] < 2:
            raise ValueError
        vec_hs = []
        rank = 0
        check = True
        i,j = 0,0
        row,col = matrix.shape
        t = min(row,col) 
        while rank < t and j < col:
            check = False
            for i in range(rank,row):
                if matrix[i,j]!=0:
                    check = True
                    vec_hs.append(j)
                    break
            if check:
                matrix[[i,rank]] = matrix[[rank,i]]
                
                matrix[rank] = matrix[rank] / matrix[rank][j]
                
                for k in range(rank+1,row):  #for(int i = rang+1;i<row;i++)
                    matrix[k]-= matrix[rank] * matrix[k][j]
                rank+=1
            j+=1

        i=0
        print(vec_hs)
        for k in vec_hs:
            for j in range(0,i):
                matrix[j]-= matrix[i] * matrix[j][k]
            i+=1
        print(matrix)
        text_result=format_matrix_output(matrix)
        result_label_transformation_special_step.config(text=text_result)
    except ValueError:
        # Show error message if input is invalid
        result_label_transformation_special_step.config(text="Invalid input")

    finally:
        print("tinh xong")
        is_transformating_special_step_matrix= False
        
is_found_projection = False
def vector_projection():
    global is_found_projection
    if is_found_projection:
        print("finding projection please wait...")
        return
    is_found_projection = True
    print("Calculate determinant button pressed") # Kiểm tra xem hàm này có được gọi đến hay không
    try:
        # Convert entries to numpy array
        #matrix = np.array([[complex(entry.get()) for entry in row] for row in matrix_entries])
        matrix=np.array(init_matrix())
        #print("Calculating determinant , matrix_entries:",matrix_entries)
        # Check if matrix has at least two rows and two columns
        if matrix.shape[0] < 2 or matrix.shape[1] < 2:
            raise ValueError
        # Calculate determinant
        vec_projection = lib_matrix.vector_projection(matrix)
        # Show result
        result_label_vector_projection.config(text=f"Vector_Projection: {vec_projection}")

    except ValueError:
        # Show error message if input is invalid
        result_label_vector_projection.config(text="Invalid input")

    finally:
        is_found_projection = False
      
        
# Create input fields and button
label1 = tk.Label(root, text="Number of rows:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Number of columns:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

create_button = tk.Button(root, text="Create matrix", command=create_matrix)
create_button.grid(row=2, column=0)

# Create calculate button and result label
calculate_button = tk.Button(root, text="Calculate determinant", command=calculate_determinant)
calculate_button.grid(row=2, column=1)

diagonal_transformation_button = tk.Button(root, text="Diagonal transformation", command=diagonal_transformation)
diagonal_transformation_button.grid(row=3, column=0)

special_transformation_button = tk.Button(root, text="special step transformation", command=transform_special_step_matrix)
special_transformation_button.grid(row=3, column=1)



vector_projection_button = tk.Button(root, text="vector_projection", command=vector_projection)
vector_projection_button.grid(row=3, column=2)

matrix_inverse_button = tk.Button(root, text="inverse_matrix", command=inverse_transform)
matrix_inverse_button.grid(row=4, column=0)

linear_system_button = tk.Button(root, text="linear_system_button", command=linear_independent_sys_vecs)
linear_system_button.grid(row=4, column=1)



# result det matrix
result_label = tk.Label(root, text="")
result_label.grid(row=99, column=0, columnspan=2)

# result transformation matrix
result_label_transformation = tk.Label(root, text="")
result_label_transformation.grid(row=98, column=0)

#result special step transformation matrix
result_label_transformation_special_step = tk.Label(root, text="")
result_label_transformation_special_step.grid(row=100, column=0)

#result vector hình chiếu
result_label_vector_projection= tk.Label(root, text="")
result_label_vector_projection.grid(row=101, column=0)

#result inverse transformation
result_label_inverse_matrix= tk.Label(root, text="")
result_label_inverse_matrix.grid(row=102, column=0)

result_label_linear_systems= tk.Label(root, text="")
result_label_linear_systems.grid(row=103, column=0)
root.mainloop()
