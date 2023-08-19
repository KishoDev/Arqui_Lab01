def suma_binaria(binario1, binario2):
    # Dividir los números binarios en partes enteras y fraccionarias
    parte_entera_binaria1, parte_fraccionaria_binaria1 = binario1.split('.')
    parte_entera_binaria2, parte_fraccionaria_binaria2 = binario2.split('.')

    # Suma de las partes enteras
    suma_parte_entera = bin(int(parte_entera_binaria1, 2) + int(parte_entera_binaria2, 2))[2:]

    # Asegurar que las partes fraccionarias tengan la misma longitud
    max_len = max(len(parte_fraccionaria_binaria1), len(parte_fraccionaria_binaria2))
    parte_fraccionaria_binaria1 = parte_fraccionaria_binaria1.ljust(max_len, '0')
    parte_fraccionaria_binaria2 = parte_fraccionaria_binaria2.ljust(max_len, '0')

    # Suma de las partes fraccionarias
    if parte_fraccionaria_binaria1 and parte_fraccionaria_binaria2:  # Solo si ambas partes fraccionarias no están vacías
        suma_parte_fraccionaria = bin(int(parte_fraccionaria_binaria1, 2) + int(parte_fraccionaria_binaria2, 2))[2:]
    else:
        suma_parte_fraccionaria = parte_fraccionaria_binaria1 or parte_fraccionaria_binaria2

    # Si hay acarreo en la parte fraccionaria, ajustar la parte entera
    if len(suma_parte_fraccionaria) > max_len:
        suma_parte_entera = bin(int(suma_parte_entera, 2) + 1)[2:]
        suma_parte_fraccionaria = suma_parte_fraccionaria[1:]

    # Combinar las partes enteras y fraccionarias para formar el número binario de suma
    suma_binaria = suma_parte_entera + '.' + suma_parte_fraccionaria
    return suma_binaria

def procesar_archivo_suma(archivo_entrada, archivo_salida):
    # Abrir archivos de entrada y salida en sus respectivos modos
    with open(archivo_entrada, 'r') as f_in, open(archivo_salida, 'w') as f_out:
        for linea in f_in:
            numero1, numero2 = linea.strip().split(';')
            resultado_suma = suma_binaria(numero1, numero2)

            # Escribir el resultado de la suma binaria en el archivo de salida
            f_out.write(f"{resultado_suma}\n")

# Nombres de archivos de entrada y salida para números positivos y negativos
archivo_entrada_positivos = "PositivosP_binario.txt"
archivo_salida_suma_positivos = "sumaP.txt"

archivo_entrada_negativos = "NegativosP_binario.txt"
archivo_salida_suma_negativos = "SumaN.txt"

# Procesar archivos de entrada y escribir resultados de suma en archivos de salida
procesar_archivo_suma(archivo_entrada_positivos, archivo_salida_suma_positivos)
procesar_archivo_suma(archivo_entrada_negativos, archivo_salida_suma_negativos)
