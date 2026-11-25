def lu_yoyilma(A):
    n = len(A)

    # Boshlang'ich U matritsa — A ning nusxasi
    U = [[float(A[i][j]) for j in range(n)] for i in range(n)]

    # Boshlang'ich L matritsa — birlik matritsa (diagonaldan 1, qolgani 0)
    L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for ustun in range(n - 1):
        tayanch = U[ustun][ustun]
        if tayanch == 0:
            raise ValueError(f"{ustun}-ustunda tayanch element 0 ga teng.")

        for qator in range(ustun + 1, n):
            kopaytiruvchi = U[qator][ustun] / tayanch
            L[qator][ustun] = kopaytiruvchi

            for k in range(ustun, n):
                U[qator][k] = U[qator][k] - kopaytiruvchi * U[ustun][k]

    return L, U


# Tekshirish uchun misol
A = [
    [5, 2, 1],
    [-10, -2, 3],
    [15, 2, -3]
]

L, U = lu_yoyilma(A)

print("L matritsa:")
for qator in L:
    print(qator)

print("\nU matritsa:")
for qator in U:
    print(qator)