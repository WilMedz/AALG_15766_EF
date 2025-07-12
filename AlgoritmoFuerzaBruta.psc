Proceso Principal
    // Definir las dimensiones de la cadena de matrices
    // Si hay m matrices, necesitamos m+1 valores en el arreglo
    Dimension dims[4]
    dims[1] <- 10
    dims[2] <- 30
    dims[3] <- 5
    dims[4] <- 60
	
    // Llamar al subproceso que calcula el orden óptimo
	MultiplicacionMatricesOptima(dims, 4)
FinProceso


SubProceso MultiplicacionMatricesOptima(dimensiones Por Referencia, tamD Por Valor)
    n <- tamD - 1
	
    // Creamos las tablas
    Dimension costos[n, n]
    Dimension divisiones[n, n]
	
    // Inicializamos la diagonal en 0
    Para i <- 1 Hasta n
        costos[i, i] <- 0
    FinPara
	
    // long es el número de matrices a multiplicar en el bloque
    Para long <- 2 Hasta n
        Para i <- 1 Hasta n - long + 1
            j <- i + long - 1
            costos[i, j] <- 999999  // Un valor grande para encontrar el mínimo
			
			Para k <- i Hasta j - 1
				costo <- costos[i, k] + costos[k+1, j] + dimensiones[i] * dimensiones[k+1] * dimensiones[j+1]

				
                Si costo < costos[i, j] Entonces
                    costos[i, j] <- costo
                    divisiones[i, j] <- k
                FinSi
            FinPara
        FinPara
    FinPara
	
    // Mostramos el costo mínimo
    Escribir "El costo mínimo es: ", costos[1, n]
	
    // Mostrar las matrices de costos y divisiones (opcional)
    Escribir ""
    Escribir "Matriz de Costos:"
    Para i <- 1 Hasta n
        Para j <- 1 Hasta n
            Escribir Sin Saltar costos[i,j], " "
        FinPara
        Escribir ""
    FinPara
	
    Escribir ""
    Escribir "Matriz de Divisiones:"
    Para i <- 1 Hasta n
        Para j <- 1 Hasta n
            Escribir Sin Saltar divisiones[i,j], " "
        FinPara
        Escribir ""
    FinPara
FinSubProceso

