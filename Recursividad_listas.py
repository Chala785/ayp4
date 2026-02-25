# Clase 19/02/2026

#  ------------ Recursividad en listas --------------

# Listas = [5,3,1,2]
# def sumar(lista):
# 	if len(lista) == 0:
# 		return 0
# 	return sumar(lista[1:]) + lista[0]
	
# Prueba de escritorio

# sumar ([5,3,1,2]) # 11
# 5 + sumar	([3,1,2]) # 6
# 3 + sumar ([1,2]) # 3 
# 1 + sumar ([2]) # 2 
# 2 + sumar ([]} #  0