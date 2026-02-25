# Clase 19/02/2026

# -------------- Funcion --------------

# def funcion (a,b):
# 	if b == 0:
# 		return 1
# 	return a * funcion(a,b-1)
# print(funcion(2,10))

# -------------- Funcion mejorada --------------

# def funcion (a,b):
# 	if b == 0:
# 		return 1
# 	if b % 2 == 0:
# 		mitad = funcion(a, b//2)
# 		return mitad * mitad
# 	else:
# 		return funcion(a,b-1)
# print(funcion(2,10))

# ------------- Palíndromo --------------

# def es_palindromo_invertir(texto):
#     limpio = texto.replace(" ", "").lower()
#     invertido = limpio[::-1]
#     return limpio == invertido
# print(es_palindromo_invertir("Anita lava la tina")) 

# ------------- Palíndromo --------------

# def es_palindromo(palabra):
#     palabra = palabra.lower()
#     inicio = 0
#     fin = len(palabra) - 1
#     while inicio < fin:
#         if palabra[inicio] != palabra[fin]:
#             return False
#         inicio += 1
#         fin -= 1
#     return True
# print(es_palindromo("Anitalavalatina"))

# ------------- Palíndromo --------------

# def es_palindromo(texto):
#     limpio = texto.replace(" ", "").lower()
#     izq = 0
#     der = len(limpio) - 1
#     while izq < der:
#         if limpio[izq] != limpio[der]:
#             return False
#         izq += 1
#         der -= 1
#     return True

# print(es_palindromo("Anitalavalatina"))

# ------------- Palíndromo recursivo --------------

# def es_palindromo_recursivo(palabra):   
#     palabra = palabra.lower()
#     if len(palabra) <= 1:
#         return True
    
#     if palabra[0] == palabra[-1]:
#         return es_palindromo_recursivo(palabra[1:-1])
#     else:
#         return False
    
# print(es_palindromo_recursivo("Anitalavalatina"))

# ------------ Palindromo a n --------------

def es_palindromo_n(palabra, inicio, fin):
    if inicio >= fin: # caso base
        return True 
    if palabra[inicio] != palabra[fin]:
        return False
    return es_palindromo_n(palabra, inicio + 1, fin - 1)









