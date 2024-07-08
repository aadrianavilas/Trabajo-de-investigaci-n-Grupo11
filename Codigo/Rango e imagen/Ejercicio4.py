def eliminacion_gauss_jordan(matriz):
    m, n = len(matriz), len(matriz[0])
    for i in range(min(m, n)):
        # Encuentra el índice del elemento máximo en la columna i para evitar divisiones entre cero.
        max_row = max(range(i, m), key=lambda r: abs(matriz[r][i]))
        if matriz[max_row][i] != 0:
            # Intercambia filas.
            matriz[i], matriz[max_row] = matriz[max_row], matriz[i]
            # Normalizar la fila i
            matriz[i] = [x / matriz[i][i] for x in matriz[i]]

            # Eliminar otras filas.
            for j in range(m):
                if i != j:
                    factor = matriz[j][i]
                    matriz[j] = [matriz[j][k] - factor * matriz[i][k] for k in range(n)]

    return matriz

def calcular_rango_y_imagen(matriz):
    # Aplicar eliminación de Gauss-Jordan a la matriz
    matriz_reducida = eliminacion_gauss_jordan(matriz)

    # Determinar el rango de la matriz
    rango = sum(1 for fila in matriz_reducida if any(abs(x) > 1e-10 for x in fila))

    # La imagen del subespacio está formada por las filas no nulas de la matriz reducida
    imagen = [fila for fila in matriz_reducida if any(abs(x) > 1e-10 for x in fila)]

    return rango, imagen

# Ejemplo de uso
matriz = [
    [1, 2],
    [3, 4 ]
    
]


rango, imagen = calcular_rango_y_imagen(matriz)

print("Rango de la matriz:", rango)
print("Imagen de la matriz:")
for fila in imagen:
    print(fila)
