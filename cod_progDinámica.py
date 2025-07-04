#codigo programacion dinamica 
def min_matriz_mult(dims):
    n = len(dims) - 1
    pd = [[0] * n for _ in range(n)]
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            pd[i][j] = float('inf')
            for k in range(i, j):
                cost = pd[i][k] + pd[k+1][j] + dims[i] * dims[k+1] * dims[j+1]
                if cost < pd[i][j]:
                    pd[i][j] = cost
                    
    return pd[0][n-1]

matrices = [
    [10, 30],  # Matriz A: 10x30
    [30, 5],   # Matriz B: 30x5
    [5, 60]    # Matriz C: 5x60
]

#  dimensiones: [10, 30, 5, 60]
dims = [matrices[0][0]] + [m[1] for m in matrices]
print(f"Mínimo de multiplicaciones: {min_matriz_mult(dims)}")