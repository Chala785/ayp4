# Tengo una lista ordenada y necesito encontrar un número en esa lista 

def busqueda_binaria(lista, num, inicio, fin):
    if inicio > fin:
        return False
    medio = (inicio + fin) // 2
    if lista[medio] == num:
        return True
    elif lista[medio] < num:
        return busqueda_binaria(lista, num, inicio, medio - 1)
    else:
        return busqueda_binaria(lista, num, medio + 1, fin)
    
    print(busqueda_binaria([2,5,8,10,12], 8, 0, 4)) 