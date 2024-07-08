# Verificar si el vector pertenece al conjunto (a)
def es_subespacio_a(vec):
    a, b, c = vec
    return a == 0 and c == 0

# Verificar si el vector pertenece al conjunto (b)
def es_subespacio_b(vec):
    a, b, c = vec
    return a == -c

# Verificar si el vector pertenece al conjunto (c)
def es_subespacio_c(vec):
    a, b, c = vec
    return b == 2*a + 1

# Verificar si un conjunto es un subespacio vectorial de R^3
def es_subespacio(conjunto, verificador):
    if len(conjunto) == 0:
        return False  # Si el conjunto está vacío, no es un subespacio

    for vec in conjunto:
        if not verificador(vec):
            return False
    
    # Verificar si contiene el vector cero
    if not verificador((0, 0, 0)):
        return False

    return True

# kolman pagina 288  ejercicio 06
conjunto_a = [(0, b, 0) for b in range(-5, 6)]  # a = 0, c = 0
conjunto_b = [(a, b, -a) for a in range(-5, 6) for b in range(-5, 6)]  # a = -c
conjunto_c = [(a, 2*a + 1, c) for a in range(-5, 6) for c in range(-5, 6)]  # b = 2a + 1

# Verificar cada conjunto
print("¿El conjunto (a) es un subespacio vectorial?", es_subespacio(conjunto_a, es_subespacio_a))
print("¿El conjunto (b) es un subespacio vectorial?", es_subespacio(conjunto_b, es_subespacio_b))
print("¿El conjunto (c) es un subespacio vectorial?", es_subespacio(conjunto_c, es_subespacio_c))
