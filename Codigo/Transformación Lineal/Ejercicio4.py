import numpy as np

def L_a(v):
    x, y = v
    return np.array([x + y, x - y])

def verificar_linealidad_a():
    # Vectores de prueba
    v1 = np.array([1, 2])
    v2 = np.array([3, 4])
    c = 2
    
    # Verificación de la aditividad
    L_v1_v2 = L_a(v1 + v2)
    L_v1_L_v2 = L_a(v1) + L_a(v2)
    
    # Verificación de la homogeneidad
    L_c_v1 = L_a(c * v1)
    c_L_v1 = c * L_a(v1)
    
    aditividad = np.allclose(L_v1_v2, L_v1_L_v2)
    homogeneidad = np.allclose(L_c_v1, c_L_v1)
    
    print("Transformación (a):")
    print("Aditividad: ", aditividad)
    print("Homogeneidad: ", homogeneidad)
    if aditividad and homogeneidad:
        print("Es una transformación lineal.")
    else:
        print("No es una transformación lineal.")

if __name__ == "__main__":
    verificar_linealidad_a()
