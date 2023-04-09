import tkinter as tk
import numpy as np
import sympy
from lib import lib_matrix
from fractions import Fraction
root = tk.Tk()
root.title("Matrix Determinant Calculator")

# Create matrix entries
matrix_entries = []
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
                entry.grid(row=i+4, column=j)
                user_input = entry.get().strip() 
                if not user_input:
            # Handle case where user input is empty
                    user_input = '0+0'
                # Tách chuỗi thành phần thực và phần ảo
                real_str, imag_str = user_input.split('+')
                real_fraction = Fraction(real_str.strip())
                imag_fraction = Fraction(imag_str.strip().replace('j', ''))
                complex_number = complex(real_fraction, imag_fraction)
                print("complex_number:",complex_number)
                row.append(complex_number)
            matrix_entries.append(row)
        print("matrix entries:",matrix_entries)
    else:
        tk.messagebox.showerror(title="Error", message="Please enter the number of rows and columns.")
        
def init_matrix(m,n):
        matrix = sympy.Matrix([[float(entry.get()) for entry in row] for row in matrix_entries])
        matrix = []
        for i in range(n):
            row = []
            for j in range(m):
                expr = input("Enter expression for matrix element a" + str(i+1) + str(j+1) + " containing x: ")
                row.append(expr)
            matrix.append(row)
        print(matrix)
        return matrix
    
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
        matrix = sympy.Matrix([[float(entry.get()) for entry in row] for row in matrix_entries])
        # Check if matrix has at least two rows and two columns
        if matrix.shape[0] < 2 or matrix.shape[1] < 2:
            raise ValueError
        matrix_res_list = lib_matrix.diagonal_transformation(matrix)
        text_result=format_matrix_output(matrix_res_list)
        result_label_transformation.config(text=text_result)
    except ValueError:
        # Show error message if input is invalid
        result_label_transformation.config(text="Invalid input")

    finally:
        #print("calculated")
        is_transformating= False
    

    

is_calculating = False
def calculate_determinant():
    
    global is_calculating
    if is_calculating:
        print("Calculating determinant please wait...")
        return
    is_calculating = True
    matrix = np.array(matrix_entries)
    print("Calculate determinant button pressed") # Kiểm tra xem hàm này có được gọi đến hay không
    try:
        # Convert entries to numpy array
        ##matrix = np.array([[complex(entry.get()) for entry in row] for row in matrix_entries])
        # Check if matrix has at least two rows and two columns
# Convert entries to numpy array of complex numbers represented as fractions
        
        print(matrix)
        
        if matrix.shape[0] < 2 or matrix.shape[1] < 2:
            raise ValueError
        # Calculate determinant
        determinant = np.linalg.det(matrix)
        print("determinant: ", determinant)
        # Show result
        result_label.config(text=f"Determinant: {determinant:.3f}")

    except ValueError:
        # Show error message if input is invalid
        result_label.config(text="Invalid input")

    finally:
        is_calculating = False

is_transformating_special_step_matrix = False
def transform_special_step_matrix():
    global is_transformating_special_step_matrix
    if is_transformating_special_step_matrix:
        print("Transformating matrix special,please wait....")
        return
    is_transformating_special_step_matrix = True
    try:
        matrix = np.array([[float(entry.get()) for entry in row] for row in matrix_entries])
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


diagonal_transformation_button = tk.Button(root, text="special step transformation", command=transform_special_step_matrix)
diagonal_transformation_button.grid(row=3, column=1)


vector_projection = tk.Button(root, text="vector_projection", command=lib_matrix.vector_projection(np.array(init_matrix())))
vector_projection.grid(row=4, column=0)

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
root.mainloop()
