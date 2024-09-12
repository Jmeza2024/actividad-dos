# Obtener los primeros n caracteres
cadena = "Python es genial"
n = 7
primeros_n = cadena[:n]
print(f"Primeros {n} caracteres: '{primeros_n}'")

# Obtener los caracteres de en medio de una cadena
cadena = "Python es genial"
inicio = len(cadena) // 2 - 2  # Ajuste para obtener una subcadena central
fin = len(cadena) // 2 + 2
medio = cadena[inicio:fin]
print(f"Caracteres del medio: '{medio}'")

# Obtener los últimos n caracteres
cadena = "Python es genial"
n = 6
ultimos_n = cadena[-n:]
print(f"Últimos {n} caracteres: '{ultimos_n}'")

