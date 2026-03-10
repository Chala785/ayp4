import re


""" ------- --------"""
# Buscar una palabra específica en un texto

# texto = "Me gusta python, es genial. Python es facil de aprender."

# resultado = re.findall("python", texto)
# print("Encontrado:", resultado)

texto = "Tengo 3 manzanaz, 12 naranjas y 100 uvas"

resultado = re.findall(r"\d+", texto)
print("Números encontrados:", resultado)