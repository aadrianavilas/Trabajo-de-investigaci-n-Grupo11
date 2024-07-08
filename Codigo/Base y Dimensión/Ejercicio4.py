def calcular_base_y_dimension(vectores):
    if not vectores:
        raise ValueError("El conjunto de vectores no puede estar vacío.")

    def es_vector_nulo(v):
        return all(x == 0 for x in v)

    vectores = [v for v in vectores if not es_vector_nulo(v)]

    if not vectores:
        return [], 0

    def eliminacion_gauss_jordan(matriz):
        if not matriz:
            return matriz

        m, n = len(matriz), len(matriz[0])
        for i in range(min(m, n)):
            max_row = max(range(i, m), key=lambda r: abs(matriz[r][i]))
            if matriz[max_row][i] != 0:
                matriz[i], matriz[max_row] = matriz[max_row], matriz[i]
                matriz[i] = [x / matriz[i][i] for x in matriz[i]]

                for j in range(m):
                    if i != j:
                        matriz[j] = [matriz[j][k] - matriz[j][i] * matriz[i][k] for k in range(n)]

        return matriz

    matriz = [list(v) for v in vectores]

    matriz_reducida = eliminacion_gauss_jordan(matriz)

    rango = sum(1 for fila in matriz_reducida if any(abs(x) > 1e-10 for x in fila))

    base = [fila[:rango] for fila in matriz_reducida if any(abs(x) > 1e-10 for x in fila)]

    dimension = rango

    return base, dimension

# Ejemplo de uso
vectores = [
    [1, 0, 2],
    [3, 1, 1],
    [-2, -1, 1],
    [5, 2, 2]
]

base, dimension = calcular_base_y_dimension(vectores)

print("Base del subespacio:")
for fila in base:
    print(fila)
print("Dimensión del subespacio:", dimension)
