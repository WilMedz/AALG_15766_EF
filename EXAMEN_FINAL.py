def multiplicacion_matrices_optima (dimensiones):
    n = len(dimensiones) - 1 
    costos = [[0] * n for _ in range(n)]
    divisiones = [[0] * n for _ in range(n)]
    
    for longitud in range(2, n + 1):  
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            costos[i][j] = float('inf')
            for k in range(i, j):
                costo_temp = (costos[i][k] + costos[k + 1][j] +
                              dimensiones[i] * dimensiones[k + 1] * dimensiones[j + 1])

                if costo_temp < costos[i][j]:
                    costos[i][j] = costo_temp
                    divisiones[i][j] = k

    return costos[0][n - 1], costos, divisiones

def parentesis_optimos(divisiones, i, j):
    if i == j:
        print(f'Matriz{i + 1}', end='')
    else:
        print('(', end='')
        parentesis_optimos(divisiones, i, divisiones[i][j])
        parentesis_optimos(divisiones, divisiones[i][j] + 1, j)
        print(')', end='')
        
    dimensiones = [10, 30, 5, 60]
    # solución óptima
    
    min_mult, costos, divisiones = multiplicacion_matrices_optima(dimensiones)

    print("\n=== solución óptima para cadena de matrices ===")
   
    print(f"número mínimo de multiplicaciones escalares: {min_mult}")
    
    #print("Parentización óptima: ", end='')
    parentesis_optimos(divisiones, 0, len(dimensiones) - 2)
    print("\n")

    print("***Tabla de Costos Mínimos***")
    for fila in costos:
        print(fila)
    
    print("\n=== tabla de divisiones Óptimas ===")
    for fila in divisiones:
        print(fila)

   
   
   
   


##codigo programacion dinamica 
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

