def eliminacion_gauss(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    for i in range(filas):
        max_el = abs(matriz[i][i])
        fila_max = i
        for k in range(i + 1, filas):
            if abs(matriz[k][i]) > max_el:
                max_el = abs(matriz[k][i])
                fila_max = k
      
        for k in range(i, columnas):
            matriz[fila_max][k], matriz[i][k] = matriz[i][k], matriz[fila_max][k] 
        
        for k in range(i + 1, filas):
            if matriz[i][i] != 0:  # Evitar división por cero
                coef = -matriz[k][i] / matriz[i][i]
                
                for j in range(i, columnas):
                    if i == j:
                        matriz[k][j] = 0
                    else:
                        matriz[k][j] += coef * matriz[i][j]
                        matriz[k][j] = round(matriz[k][j], 2)
    return matriz

def es_linealmente_independiente(vectores):
    # Crear la matriz aumentada
    matriz = [list(vector) for vector in zip(*vectores)]
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_reducida = eliminacion_gauss(matriz)
    print(matriz_reducida) 
    # Verificar si hay filas de ceros en la parte reducida
    for fila in matriz_reducida:
        if all(abs(x) < 1e-10 for x in fila):  
            return False
    
    if filas != columnas: 
        return False
    else:
        return True

# Definir vectores
v1 = (1,2,3)
v2 = (2,-2,0)
v3 = (0,1,7)

# Verificar la independencia lineal
vectores = [v1, v2, v3]
if es_linealmente_independiente(vectores):
    print("Son linealmente independientes.")
else:
    print("Son linealmente dependientes.")