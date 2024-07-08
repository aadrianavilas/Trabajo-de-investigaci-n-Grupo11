def es_base_R2(v1, v2):
    if len(v1) != 2 or len(v2) != 2:
        return False

    determinante = v1[0] * v2[1] - v1[1] * v2[0]

    return determinante != 0

v1 = [1, 3]
v2 = [1, -1]

if es_base_R2(v1, v2):
    print("El conjunto {v1, v2} forma una base en R^2.")
else:
    print("El conjunto {v1, v2} no forma una base en R^2.")
