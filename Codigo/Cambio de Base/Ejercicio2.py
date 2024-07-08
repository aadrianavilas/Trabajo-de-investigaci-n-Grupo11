import sympy as sp

# Definir variables simbólicas
x, y = sp.symbols('x y')

# Definir la base
B = sp.Matrix([[1, 1], [1, -1]])

# Invertir la matriz de la base
B_inv = B.inv()

# Definir el vector
v = sp.Matrix([x, y])

# Calcular el vector en la nueva base
v_new_base = B_inv * v

# Mostrar el resultado
print(f"El vector ({x}, {y}) en la nueva base es: {v_new_base}")

