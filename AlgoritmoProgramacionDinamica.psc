Proceso Principal
    Dimension dims[4]
    dims[1] <- 10
    dims[2] <- 30
    dims[3] <- 5
    dims[4] <- 60
	
    costoMin <- 0
    MultiplicacionMatricesOptima(dims, 4, costoMin)
    Escribir "El costo mínimo es: ", costoMin
FinProceso
SubProceso MultiplicacionMatricesOptima(dimensiones Por Referencia, tamD Por Valor, resultado Por Referencia)
    n <- tamD - 1
    Dimension pd[10, 10]
	
    Para i <- 1 Hasta n
        pd[i, i] <- 0
    FinPara
	
    Para long <- 2 Hasta n
        Para i <- 1 Hasta n - long + 1
            j <- i + long - 1
            pd[i, j] <- 999999
			
            Para k <- i Hasta j - 1
                costo <- pd[i, k] + pd[k+1, j] + dimensiones[i] * dimensiones[k+1] * dimensiones[j+1]
				
                Si costo < pd[i, j] Entonces
                    pd[i, j] <- costo
                FinSi
            FinPara
        FinPara
    FinPara
	
    resultado <- pd[1, n]  // Así "retornas" el resultado
FinSubProceso
