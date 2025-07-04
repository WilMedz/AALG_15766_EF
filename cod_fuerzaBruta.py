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

print("\n*** SOLUCION OPTIMA ***")
   
print(f"Número mínimo de multiplicaciones: \n {min_mult}")
    
print("\n***Costos Mínimos***")
for fila in costos:
    print(fila)
    
print("\n*** Divisiones Óptimas ***")
for fila in divisiones:
    print(fila)