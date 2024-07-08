def combinacion_lineal(coeficientes, vectores):
   
    resultado = [0] * len(vectores[0])
    for c, v in zip(coeficientes, vectores):
        for i in range(len(v)):
            resultado[i] += c * v[i]
    
    return resultado

c1, c2= 2,-1

# Definir vectores
v1 = (-1,2,4)
v2 = (5,-3,1)



coeficientes = [c1, c2]
vectores = [v1, v2]
resultado = combinacion_lineal(coeficientes, vectores)

# Mostrar el resultado
print("La combinación lineal es:", resultado)