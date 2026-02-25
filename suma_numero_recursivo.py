# Clase 19/02/2026

# Tenemos un número, un algoritmo que sea recursivo que sume los dígitos de ese número

def suma_digitos(n):
    if n == 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

print(suma_digitos(1503))