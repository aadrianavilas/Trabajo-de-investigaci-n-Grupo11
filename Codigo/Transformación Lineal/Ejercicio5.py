import numpy as np

def L_b(v):
    x, y, z = v
    return np.array([x + 1, y - z])

def verificar_linealidad_b():
    # Vectores de prueba
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    c = 2
    
    # Verificación de la aditividad
    L_v1_v2 = L_b(v1 + v2)
    L_v1_L_v2 = L_b(v1) + L_b(v2)
    
    # Verificación de la homogeneidad
    L_c_v1 = L_b(c * v1)
    c_L_v1 = c * L_b(v1)
    
    aditividad = np.allclose(L_v1_v2, L_v1_L_v2)
    homogeneidad = np.allclose(L_c_v1, c_L_v1)
    
    print("Transformación (b):")
    print("Aditividad: ", aditividad)
    print("Homogeneidad: ", homogeneidad)
    if aditividad and homogeneidad:
        print("Es una transformación lineal.")
    else:
        print("No es una transformación lineal.")

if __name__ == "__main__":
    verificar_linealidad_b()
