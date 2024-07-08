def es_base_R3(v1, v2, v3):
    if len(v1) != 3 or len(v2) != 3 or len(v3) != 3:
        return False

    # Calcular el determinante de la matriz formada por los tres vectores
    determinante = (
        v1[0] * (v2[1] * v3[2] - v2[2] * v3[1])
        - v1[1] * (v2[0] * v3[2] - v2[2] * v3[0])
        + v1[2] * (v2[0] * v3[1] - v2[1] * v3[0])
    )

    return determinante != 0

# Ejemplo de uso
v1 = [1, 0, 0]
v2 = [0, 2, -1]
v3 = [0,1, 0]

if es_base_R3(v1, v2, v3):
    print(f"El conjunto {{v1, v2, v3}} forma una base en R^3.")
else:
    print(f"El conjunto {{v1, v2, v3}} no forma una base en R^3.")
