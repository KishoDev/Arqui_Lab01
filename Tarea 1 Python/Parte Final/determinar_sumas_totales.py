no_se_pudo = 0
si_se_pudo = 0
total = 0

try:
    with open("resultado.txt", "r") as archivo:
        for linea in archivo:
            total += 1
            if ";" in linea:
                no_se_pudo += 1
            else:
                si_se_pudo += 1
except FileNotFoundError:
    print("El archivo 'prueba.txt' no se encontró.")

print("Resultados:")
print("Total de líneas analizadas:", total)
print("Líneas con ';' (no se pudo):", no_se_pudo)
print("Líneas sin ';' (sí se pudo):", si_se_pudo)
