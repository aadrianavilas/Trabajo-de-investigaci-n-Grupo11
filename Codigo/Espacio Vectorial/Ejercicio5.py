def suma_vectores(u, v):

    if len(u) != 2 or len(v) != 2:
        raise ValueError("Los vectores deben ser tuplas de tres elementos (x, y, 0).")

    return (u[0] + v[0], u[1] + v[1])

def elemento_neutro():
    return (0, 0)

def inverso_aditivo(u):

    if len(u) != 2 :
        raise ValueError("El vector debe ser una tupla de tres elementos (x, y, 0).")

    return (-u[0], -u[1])

def multiplicacion_escalar(c, u):

    if len(u) != 2:
        raise ValueError("El vector debe ser una tupla de tres elementos (x, y, 0).")

    return (c * u[0], c * u[1])


# Axioma 01: Verificación de suma y pertenencia
def verificar_axioma_1(u, v):
    print("********************************")
    print("Axioma 1:")
    print("(x1,y1) ⊕ (x2,y2) = (x1+x2, y1+y2)")
    print()

    print("Definición:")
    print("Si u y v pertenecen a vectores en ℝ², entonces u ⊕ v también pertenece a ℝ².")
    print()

    print("Vectores de entrada:")
    print(f"u = {u}")
    print(f"v = {v}")
    print()

    resultado_suma = suma_vectores(u, v)

    print("Resultado de la suma:")
    print(f"u ⊕ v = {resultado_suma} también pertenece a vectores de ℝ²")
    print("Si cumple")
    print("")
    return isinstance(resultado_suma, tuple) and len(resultado_suma) == 2

# Axioma 02: Conmutación
def verificar_axioma_2(u, v):
    print("********************************")
    print("Axioma 2:")
    print("(x,y,z) ⊕ (x',y',z') = (x',y',z') ⊕ (x,y,z)")
    print()

    print("Definición:")
    print("Si u y v pertenecen a vectores en ℝ² con tercer, entonces u ⊕ v = v ⊕ u.")
    print()

    print("Vectores de entrada:")
    print(f"u = {u}")
    print(f"v = {v}")
    print()

    resultado1 = suma_vectores(u, v)
    resultado2 = suma_vectores(v, u)

    print("Resultado de la suma:")
    print(f"u ⊕ v = {resultado1}")
    print(f"v ⊕ u = {resultado2}")

    cumple = resultado1 == resultado2
    print(f"Si cumple: {cumple}")
    print("")

    return cumple


def verificar_axioma_3(u, v, w):
    # Imprimir axioma
    print("********************************")
    print("Axioma 3:")
    print("Para todo u, v y w pertenecientes a vectores en ℝ² tal que:")
    print("u ⊕ (v ⊕ w) = (u ⊕ v) ⊕ w")
    print()

    # Definición matemática
    print("Definición:")
    print("Si u, v y w son vectores en ℝ², entonces el orden de los sumandos no afecta al resultado de la suma.")
    print()

    # Imprimir los vectores de entrada
    print("Vectores de entrada:")
    print(f"u = {u}")
    print(f"v = {v}")
    print(f"w = {w}")
    print()

    # Calculamos los resultados de las sumas
    resultado1 = suma_vectores(suma_vectores(u, v), w)
    resultado2 = suma_vectores(u, suma_vectores(v, w))

    # Imprimimos los resultados de las sumas
    print("Resultados de las sumas:")
    print(f"(u ⊕ v) ⊕ w = {resultado1}")
    print(f"u ⊕ (v ⊕ w) = {resultado2}")

    # Verificamos si se cumple el axioma
    cumple = resultado1 == resultado2
    print(f"Si cumple: {cumple}")
    print("")

    return cumple

def verificar_axioma_4(u):
    # Encuentra el elemento neutro
    neutro = elemento_neutro()

    # Imprimir axioma
    print("********************************")
    print("Axioma 4:")
    print("u ⊕ (0, 0, 0) = (0, 0, 0) ⊕ u = u")
    print()

    # Definición matemática
    print("Definición:")
    print("Existe un elemento neutro (0, 0, 0) tal que para todo vector u en ℝ²")
    print("tal que u ⊕ (0, 0, 0) = (0, 0, 0) ⊕ u = u ")
    print()

    # Imprimir el vector u
    print("Vector u:")
    print(f"u = {u}")
    print()

    # Calculamos los resultados de las sumas con el elemento neutro
    resultado1 = suma_vectores(u, neutro)
    resultado2 = suma_vectores(neutro, u)

    # Imprimimos los resultados de las sumas
    print("Resultados de las sumas:")
    print(f"u ⊕ (0, 0, 0) = {resultado1}")
    print(f"(0, 0, 0) ⊕ u = {resultado2}")
    cumple = resultado1 == resultado2
    print(f"Si cumple: {cumple}")
    print("")
    return cumple

def verificar_axioma_5(u):

    # Encuentra el inverso aditivo de u
    inverso_u = inverso_aditivo(u)
    neutro = elemento_neutro()
    # Imprimir axioma
    print("********************************")
    print("Axioma 5:")
    print("u ⊕ (-u) = (0, 0, 0)")
    print()

    # Definición matemática
    print("Definición:")
    print("Existe un elemento -u tal que para todo vector u en ℝ² cumpla con u ⊕ (-u) = (0, 0, 0)")
    print()

    # Imprimir el vector u
    print("Vector u:")
    print(f"u = {u}")
    print(f"-u = {inverso_u}")
    print()

    # Calculamos el resultado de la suma con el inverso aditivo
    resultado = suma_vectores(u, inverso_u)

    # Imprimimos el resultado de la suma
    print("Resultado de la suma:")
    print(f"u ⊕ (-u) = {resultado}")

    cumple = neutro == resultado
    print(f"Si cumple: {cumple}")
    print("")
    return cumple

def  verificar_axioma_6(c, u):

    # Calculamos el resultado de la multiplicación escalar
    resultado = multiplicacion_escalar(c, u)

    # Imprimir axioma
    print("********************************")
    print("Axioma 6:")
    print("c ⊙ u ∈ V")
    print()

    # Definición matemática
    print("Definición:")
    print("Si u es un elemento de ℝ²  c es un número real, entonces c ⊙ u también es un elemento de ℝ² ")
    print()

    # Imprimir el vector u y el escalar c
    print("Vector u:")
    print(f"u = {u}")
    print()
    print("Escalar c:")
    print(f"c = {c}")
    print()

    # Imprimimos el resultado de la multiplicación escalar
    print("Resultado de la multiplicación escalar:")
    print(f"c ⊙ u = {resultado}")
    print(f"Tambien es un elemento de ℝ² /cumple")
    print("")
    return True

def  verificar_axioma_7(c, d, u):

    # Calculamos los resultados de las operaciones según el axioma
    resultado1 = multiplicacion_escalar(c + d, u)
    resultado2 = suma_vectores(multiplicacion_escalar(c, u), multiplicacion_escalar(d, u))

    # Imprimir axioma
    print("Axioma 7:")
    print("(c ⊕ d) ⊙ u = c ⊙ u ⊕ d ⊙ u")
    print()

    # Definición matemática
    print("Definición:")
    print("Para todo número real c y d, y para todo vector u en ℝ² tal que (c ⊕ d) ⊙ u = c ⊙ u ⊕ d ⊙ u.")
    print()

    # Imprimir el vector u y los escalares c, d
    print("Vector u:")
    print(f"u = {u}")
    print()
    print("Escalares c, d:")
    print(f"c = {c}")
    print(f"d = {d}")
    print()

    # Imprimimos los resultados de las operaciones
    print("Resultados de las operaciones:")
    print(f"(c ⊕ d) ⊙ u = {resultado1}")
    print(f"c ⊙ u ⊕ d ⊙ u = {resultado2}")
    cumple  = resultado1 == resultado2
    print(f"Si cumple:{cumple}")
    print("")
    return cumple



def  verificar_axioma_8(c, u, v):

    # Calculamos los resultados de las operaciones según el axioma
    resultado1 = multiplicacion_escalar(c, suma_vectores(u, v))
    resultado2 = suma_vectores(multiplicacion_escalar(c, u), multiplicacion_escalar(c, v))

    # Imprimir axioma
    print("Axioma 8:")
    print("c ⊙ (u ⊕ v) = c ⊙ u ⊕ c ⊙ v")
    print()

    # Definición matemática
    print("Definición:")
    print("Para todo número real c y para todos los vectores u, v en ℝ² con tercer componente fijo en 0, se cumple que c ⊙ (u ⊕ v) = c ⊙ u ⊕ c ⊙ v.")
    print()

    # Imprimir los vectores u, v y el escalar c
    print("Vectores u, v:")
    print(f"u = {u}")
    print(f"v = {v}")
    print()
    print("Escalar c:")
    print(f"c = {c}")
    print()

    # Imprimimos los resultados de las operaciones
    print("Resultados de las operaciones:")
    print(f"c ⊙ (u ⊕ v) = {resultado1}")
    print(f"c ⊙ u ⊕ c ⊙ v = {resultado2}")
    cumple   = resultado1  == resultado2
    print(f"Si cumple: {cumple}")
    return cumple



def  verificar_axioma_9(c, d, u):

    resultado1 = multiplicacion_escalar(c + d, u)
    resultado2 = suma_vectores(multiplicacion_escalar(c, u), multiplicacion_escalar(d, u))

    # Imprimir axioma
    print("Axioma 8:")
    print("c ⊙ (u ⊕ v) = c ⊙ u ⊕ c ⊙ v")
    print()

    # Definición matemática
    print("Definición:")
    print("Para todo número real c y para todos los vectores u, v en ℝ tal que c ⊙ (u ⊕ v) = c ⊙ u ⊕ c ⊙ v.")
    print()

    # Imprimir los vectores u, v y el escalar c
    print("Vectores u, v:")
    print(f"u = {u}")
    print(f"v = {v}")
    print()
    print("Escalar c:")
    print(f"c = {c}")
    print()

    # Imprimimos los resultados de las operaciones
    print("Resultados de las operaciones:")
    print(f"c ⊙ (u ⊕ v) = {resultado1}")
    print(f"c ⊙ u ⊕ c ⊙ v = {resultado2}")
    cumple  = resultado1 == resultado2
    print(f"Si cumple:{cumple}")
    print("")
    return cumple



def verificar_axioma_10(c,u):

    # Calculamos el resultado de la operación según el axioma
    resultado = multiplicacion_escalar(c, u)

    # Imprimir axioma
    print("Axioma 10:")
    print("Para toda u en ℝ²  tal que 1 ⊙ u = u.")
    print()

    # Definición matemática
    print("Definición:")
    print("1 ⊙ u = u")
    print()

    # Imprimir el vector u y el escalar c
    print("Vector u:")
    print(f"u = {u}")
    print()
    print("Escalar c:")
    print(f"c = {c}")
    print()

    # Imprimir el resultado de la operación
    print("Resultado de la operación:")
    print(f"1 ⊙ u = {resultado}")
    cumple   = u == resultado
    print(f"Si cumple:{cumple}")
    print("")
    return cumple


if __name__ == "__main__":
    # Definición de vectores
    u = (5, 2)
    v = (4, 2)
    w = (1, 3)

    c = 2 # valor escalar
    d = 4 # valor escalar
    e = 1 # valor escalar

    #Verificar axiomas
    resultado_axioma_1 = verificar_axioma_1(u, v)
    resultado_axioma_2 = verificar_axioma_2(u, v)
    resultado_axioma_3 = verificar_axioma_3(u, v, w)
    resultado_axioma_4 = verificar_axioma_4(u)
    resultado_axioma_5 = verificar_axioma_5(u)
    resultado_axioma_6 = verificar_axioma_6(c,u)
    resultado_axioma_7 = verificar_axioma_7(c,d,u)
    resultado_axioma_8 = verificar_axioma_8(c,u,v)
    resultado_axioma_9 = verificar_axioma_9(c,d,u)
    resultado_axioma_10 = verificar_axioma_10(e,u)


# # Mostrar resultados individuales de cada axioma
print("Resultados de los axiomas:")
print(f"Axioma 1: {resultado_axioma_1}")
print(f"Axioma 2: {resultado_axioma_2}")
print(f"Axioma 3: {resultado_axioma_3}")
print(f"Axioma 4: {resultado_axioma_4}")
print(f"Axioma 5: {resultado_axioma_5}")
print(f"Axioma 6: {resultado_axioma_6}")
print(f"Axioma 7: {resultado_axioma_7}")
print(f"Axioma 8: {resultado_axioma_8}")
print(f"Axioma 9: {resultado_axioma_9}")
print(f"Axioma 10: {resultado_axioma_10}")

# # Verificar si todos los resultados son True
if (
    resultado_axioma_1 and
    resultado_axioma_2 and
    resultado_axioma_3 and
    resultado_axioma_4 and
    resultado_axioma_5 and
    resultado_axioma_6 and
    resultado_axioma_7 and
    resultado_axioma_8 and
    resultado_axioma_9 and
    resultado_axioma_10
):
    print("Todos los axiomas son verdaderos. Es un espacio vectorial.")
else:
    print("No todos los axiomas son verdaderos. No es un espacio vectorial.")