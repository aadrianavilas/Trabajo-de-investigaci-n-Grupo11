import numpy as np

def L(vector):
    return np.array([0, 0])

# Verificación de la propiedad de adición
def verificar_adicion():
    u = np.array([1, 2, 3])
    v = np.array([4, 5, 6])
    return np.allclose(L(u + v), L(u) + L(v))

# Verificación de la propiedad de escalado
def verificar_escalado():
    u = np.array([1, 2, 3])
    c = 2
    return np.allclose(L(c * u), c * L(u))

# Verificar linealidad
is_linear = verificar_adicion() and verificar_escalado()

print(f"La transformación es {'lineal' if is_linear else 'no lineal'}")
