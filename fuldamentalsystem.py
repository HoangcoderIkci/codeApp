import numpy as np


def solve_homogeneous_system(arr):
    A = np.round(np.array(arr,dtype=float),2)
    print("solve A:", A)
    j = 0
    rank = 0
    m = len(A)
    n = len(A[0])
    miN = min(m, n)
    vector_hs = []
    while j < n and rank < miN:
        check = False
        for i in range(rank, m):
            if (A[i][j] != 0):
                check = True
                A[i] = (A[i] / A[i][j])
                A[i] = np.round(A[i],decimals=2)
                temp = np.array(A[i])
                A[i] = np.array(A[rank])
                A[rank] = np.array(temp)
                break
        if (check == True):
            for i in range(rank+1, m):
                if (A[i][j] != 0):
                    A[i] -= (A[rank]*A[i][j])
                    A[i] =np.round(A[i],decimals=2)
            rank += 1
            vector_hs.append(j)
        j += 1
        print(A)
# ========== end step-1===========
# =========== step-2 change matrix to special step matrix============
    k = rank-1
    vec_reversed = list(reversed(vector_hs))
    print(vec_reversed)
    for itr in vec_reversed:
        for i in range(0, k):
            if (A[i][itr] == 0):
                continue
            A[i] -= A[k]*A[i][itr]
            A[i] = np.round(A[i],decimals=2)
        k -= 1
        print(A)
    print(A.T)
# ========== END step-2===============#
# ========== Step-3 get solutions========#
    my_filter = [True] * n
    for itr in vector_hs:
        my_filter[itr] = False
    my_hs_free = np.arange(n)
    #print("my_hs_free",my_hs_free)
    my_hs_free = my_hs_free[my_filter]
    #print("my_hs_free",my_hs_free)
    A_filtered = (A.T)[my_filter]
    #print(f'A_filtered{A_filtered}')
    dim_system_fcr = len(A_filtered)
    new_length = m-n
    if m!=n:
        nul_array = np.zeros((new_length, new_length))
    #print(f'A[0]={A_filtered}')
        print(f"A_filtered{A_filtered}")
        print(f"nul_array{nul_array}")
        A_filtered = np.concatenate((A_filtered, nul_array), axis=1)
    for i in range(dim_system_fcr):
        A_filtered[i][my_hs_free[i]] = -1
    return A_filtered


A = np.array([[-2,-2,8],[-2,7,-10],[8,-10,4]])
solution = solve_homogeneous_system(A)

print("solution:",solution)
print(A)