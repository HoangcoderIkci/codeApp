from fractions import Fraction as frac
import numpy as np

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
            v_conjugate = v.conjugate()
            u -= np.dot(u, v) / np.dot(v, v_conjugate) * v
        if np.linalg.norm(u) > 1e-10:
            u /= np.linalg.norm(u)
        ortho_vectors.append(u)
    # Convert the resulting vectors to complex with fractions
    ortho_vectors_complex = []
    # ortho_vector_complex = []
    # print(len(ortho_vectors[0]))
    for row in ortho_vectors:
        ortho_vector_complex = []
        for v in row:
            real_part = frac(v.real).limit_denominator(10)
            imag_part = frac(v.imag).limit_denominator(10)
            ortho_vector_complex.append(complex(real_part, imag_part))
        ortho_vectors_complex.append(ortho_vector_complex)

    return ortho_vectors_complex


# =============== Dau vao la system vectors u and vector alpha============
# u1 = np.array([frac(3, 5) + frac(4, 7)*1j, frac(1, 2) + frac(2, 3)*1j])
# u2 = np.array([frac(5, 8) - frac(2, 9)*1j, frac(3, 4) - frac(1, 6)*1j])
# # v3 = np.array([frac(2, 3) + frac(1, 4)*1j, frac(4, 5) - frac(3, 8)*1j])
# ortho_basis = gram_schmidt([u1, u2])
# # ortho_basis_fraction = [[print(f'{frac(v.real).limit_denominator(10)}+{frac(v.imag).limit_denominator(10)}j')
# #                          for v in row_of_ortho_basis] for row_of_ortho_basis in ortho_basis]
# print_format_fraction(ortho_basis)
# # ========== result last vector of ortho_basis=========#
# projection_vector_alpha = ortho_basis[-1]
# [print(f'({frac(x.real).limit_denominator(10)}+{frac(x.imag).limit_denominator(10)}j)', end='  ')
#  for x in projection_vector_alpha]
