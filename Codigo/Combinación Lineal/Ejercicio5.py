def combinacion_lineal(coeficientes, vectores):
   
    resultado = [0] * len(vectores[0])
    for c, v in zip(coeficientes, vectores):
        for i in range(len(v)):
            resultado[i] += c * v[i]
    
    return resultado

c1, c2,c3= 1,2,-1

# Definir vectores
v1 = (1,2,1)
v2 = (1,0,2)
v3 = (1,1,0)



coeficientes = [c1, c2,c3]
vectores = [v1, v2,v3]
resultado = combinacion_lineal(coeficientes, vectores)

# Mostrar el resultado
print("La combinación lineal es:", resultado)