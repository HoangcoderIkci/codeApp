import tkinter as tk
import numpy as np
from fractions import Fraction


root = tk.Tk()
root.title("Matrix calculate Beta by Hoang-Ikci")

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
                entry.grid(row=i+6, column=j)
                row.append(entry)
            matrix_entries.append(row)
            #print("called, matrix entries:",matrix_entries)
    else:
        tk.messagebox.showerror(title="Error", message="Please enter the number of rows and columns.")
     
     
# Create matrix entries
matrix_entries_2 = []
num_rows_2 = 0
num_cols_2 = 0
def create_matrix_2():
    # Clear previous matrix entries
    for row in matrix_entries_2:
        for entry in row:
            entry.destroy()
    matrix_entries_2.clear()

    # Get number of rows and columns
    num_rows_2 = entry1_2.get()
    num_cols_2 = entry2_2.get()
    #print(num_cols,num_rows)
    # Check if input fields are not empty
    if num_rows_2 and num_cols_2:
        num_rows_2 = int(num_rows_2)
        num_cols_2 = int(num_cols_2)
        for i in range(num_rows_2):
            row = []
            for j in range(num_cols_2):
                entry = tk.Entry(root)
                entry.grid(row=i+56, column=j)
                row.append(entry)
            matrix_entries_2.append(row)
            #print("called, matrix entries:",matrix_entries)
    else:
        tk.messagebox.showerror(title="Error", message="Please enter the number of rows and columns.")     
     
     
     
     
     
     
     
     
     
     
        
def init_matrix(n,m,which_matrix):
    if which_matrix==0:
        matrix_entries_copy = matrix_entries.copy()
    else: matrix_entries_copy = matrix_entries_2.copy()
    matrix_results = []
    for row in matrix_entries_copy:
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
                text_result+= '{0:.{1}f}'.format(element,2) + "     "
            text_result += '\n\n'
    return text_result
            

    
    
is_finding_det_matrix = False

def calculate_determinant(which_matrix):
    
    global is_finding_det_matrix
    if is_finding_det_matrix:
        print("Calculating determinant please wait...")
        return
    is_finding_det_matrix = True
    print("Calculate determinant button pressed") # Kiểm tra xem hàm này có được gọi đến hay không
    try:
        if which_matrix == 0:
            matrix=np.array(init_matrix(num_rows,num_cols ,which_matrix))
        else: matrix=np.array(init_matrix(num_rows_2,num_cols_2 ,which_matrix))
        #print("Calculating determinant , matrix_entries:",matrix_entries)
        # Check if matrix has at least two rows and two columns
        if matrix.shape[0] < 2 or matrix.shape[1] < 2:
            raise ValueError
        # Calculate determinant
        determinant = np.linalg.det(matrix)
        print("determinant: ", determinant)
        # Show resultis_finding det_matrix
        result_label.config(text=f"Determinant of matrix {which_matrix}   : {determinant:.3f}")

    except ValueError:
        # Show error message if input is invalid
        result_label.config(text="Invalid input")

    finally:
        is_finding_det_matrix = False



is_operating = False

def Operator_matrix():
    
    global is_operating
    if is_operating:
        print("Calculating multiple please wait...")
        return
    is_operating = True
    print("Calculate multiple button pressed") # Kiểm tra xem hàm này có được gọi đến hay không
    try:
        # Convert entries to numpy array
        #matrix = np.array([[complex(entry.get()) for entry in row] for row in matrix_entries])
        operator = entry_operator.get()
        matrix_first=np.array(init_matrix(num_rows,num_cols,0))
        matrix_second=np.array(init_matrix(num_rows_2,num_cols_2,1))
        #print("Calculating determinant , matrix_entries:",matrix_entries)
        # Check if matrix has at least two rows and two columns
        if operator ==  "*":
                if matrix_first.shape[1] !=  matrix_second.shape[0]:
                    raise ValueError
        # Calculate determinant
                matrix_result = matrix_first @ matrix_second
        elif operator ==  "+":
                if matrix_first.shape != matrix_second.shape:
                    raise ValueError
                matrix_result = matrix_first + matrix_second
        elif operator ==  '-':
                if matrix_first.shape != matrix_second.shape:
                    raise ValueError
                matrix_result = matrix_first - matrix_second
                
                
        print(f"A{operator}B = : ", matrix_result)
        # Show resultis_finding det_matrix
        result_label_multiple.config(text=f"Matrix A{operator}B   : \n {format_matrix_output(matrix_result)}")

    except ValueError:
        # Show error message if input is invalid
        result_label_multiple.config(text="Invalid input")

    finally:
        is_operating = False

is_pow = False

def pow_matrix():
    
    global is_pow
    if is_pow:
        print("pow please wait...")
        return
    is_pow = True
    print("Pow button pressed") # Kiểm tra xem hàm này có được gọi đến hay không
    try:
        # Convert entries to numpy array
        #matrix = np.array([[complex(entry.get()) for entry in row] for row in matrix_entries])
        #operator = entry_operator.get()
        #matrix_first=np.array(init_matrix(num_rows,num_cols,0))
        info_which_matrix = entry_pow.get()
        str_which_matrix,degree_matrix = info_which_matrix.split('^')
        if str_which_matrix == 'A':
            which_matrix = 0
        elif str_which_matrix == 'B':
            which_matrix = 1
        degree = int(degree_matrix)
        matrix=np.array(init_matrix(num_rows_2,num_cols_2,which_matrix))
        matrix_pow = np.linalg.matrix_power(matrix,degree)
        result_label_pow.config(text=f"Matrix {str_which_matrix}^{degree}   : \n {format_matrix_output(matrix_pow)}")
    except ValueError:
        # Show error message if input is invalid
        result_label_pow.config(text="Invalid input")

    finally:
        is_pow = False
 
# Create input fields and button
label1 = tk.Label(root, text="Number of rows:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Number of columns:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)


label_operator = tk.Label(root, text="Operator")
label_operator.grid(row=0, column=3)
entry_operator = tk.Entry(root)
entry_operator.grid(row=0, column=4)

label_pow = tk.Label(root, text="Pow")
label_pow.grid(row=1, column=3)
entry_pow = tk.Entry(root)
entry_pow.grid(row=1, column=4)


label1_2 = tk.Label(root, text="Number of rows:")
label1_2.grid(row=50, column=0)
entry1_2 = tk.Entry(root)
entry1_2.grid(row=50, column=1)

label2_2 = tk.Label(root, text="Number of columns:")
label2_2.grid(row=51, column=0)
entry2_2 = tk.Entry(root)
entry2_2.grid(row=51, column=1)



create_button = tk.Button(root, text="Create matrix", command=create_matrix)
create_button.grid(row=2, column=0)


create_button_2 = tk.Button(root, text="Create matrix_2", command=create_matrix_2)
create_button_2.grid(row=52, column=0)

multiple_matrix_button = tk.Button(root, text="submit", command=Operator_matrix)
multiple_matrix_button.grid(row=0, column=5)

pow_matrix_button = tk.Button(root, text="pow", command=pow_matrix)
pow_matrix_button.grid(row=1, column=5)


# Create calculate button and result label
calculate_button = tk.Button(root,text="Calculate determinant", command=lambda:calculate_determinant(0))
calculate_button.grid(row=2, column=1)

calculate_button = tk.Button(root,text="Calculate determinant_2",command=lambda: calculate_determinant(1))
calculate_button.grid(row=52, column=1)

# result det matrix
result_label = tk.Label(root, text="")
result_label.grid(row=100, column=0, columnspan=2)

result_label_multiple = tk.Label(root, text="")
result_label_multiple.grid(row=117, column=0, columnspan=2)

result_label_pow = tk.Label(root, text="")
result_label_pow.grid(row=118, column=0, columnspan=2)



root.mainloop()

