def es_subespacio(subconjunto, operacion):
   for p in subconjunto:
    for q in subconjunto:
      resultado = operacion(p, q)
      existe_equivalente = False
      for r in subconjunto:
        if resultado[0] + list(r)[0] == 0 and resultado[1] + list(r)[1] == 0 and resultado[2] + list(r)[2] == 0:
            existe_equivalente = True
            break
        if not existe_equivalente:
            return False
    return True

def suma_polinomios(p1, p2):
  (a21, a11, a01), (a22, a12, a02) = p1, p2
  return (a21 + a22, a11 + a12, a01 + a02)

def producto_escalar(p, escalar):
  (a2, a1, a0) = p
  return (escalar * a2, escalar * a1, escalar * a0)
 
# Kolman pagina 288  ejercicio 10 

subconjunto_a = [(a2, a1, a0) for a2, a1, a0 in zip(range(-10, 11), range(-10, 11), range(-10, 11))if a1 == 0 and a0 == 0] # a1 = 0 y a0 = 0
subconjunto_b = [(a2, a1, a0) for a2, a1, a0 in zip(range(-10, 11), range(-10, 11), range(-10, 11))if a1 == 2*a0]  # a1 = 2a0
subconjunto_c = [(a2, a1, a0) for a2, a1, a0 in zip(range(-10, 11), range(-10, 11), range(-10, 11))if a2 + a1 + a0 == 2]  # a2 + a1 + a0 = 2

# Evaluamos si cada subconjunto es un subespacio
print(f"Subconjunto A: {es_subespacio(subconjunto_a, suma_polinomios)}")
print(f"Subconjunto B: {es_subespacio(subconjunto_b, suma_polinomios)}")
print(f"Subconjunto C: {es_subespacio(subconjunto_c, suma_polinomios)}")