def decimal_a_binario(numero_decimal):
    # Separar la parte entera y la parte fraccionaria del número decimal
    parte_entera = int(numero_decimal)
    parte_fraccionaria = numero_decimal - parte_entera

    # Convertir la parte entera a binario
    parte_entera_binaria = bin(parte_entera)[2:]  # [2:] para eliminar el prefijo "0b"

    # Convertir la parte fraccionaria a binario
    parte_fraccionaria_binaria = ''
    contador = 0

    # Convertir la parte fraccionaria a binario hasta alcanzar 20 bits o llegar a un valor cercano a cero
    while parte_fraccionaria > 0.0001 and contador < 20:
        parte_fraccionaria *= 2
        bit = int(parte_fraccionaria)
        parte_fraccionaria_binaria += str(bit)
        if parte_fraccionaria >= 1:
            parte_fraccionaria -= 1
        contador += 1

    # Combinar las partes enteras y fraccionarias para formar el número binario completo
    numero_binario = parte_entera_binaria + '.' + parte_fraccionaria_binaria
    return numero_binario

def procesar_archivo(archivo_entrada, archivo_salida):
    # Abrir archivos de entrada y salida en sus respectivos modos
    with open(archivo_entrada, 'r') as f_in, open(archivo_salida, 'w') as f_out:
        for linea in f_in:
            numero1, numero2 = linea.strip().split(';')
            numero1_decimal = float(numero1)
            numero2_decimal = float(numero2)

            # Convertir los números decimales a binario utilizando la función decimal_a_binario
            numero1_binario = decimal_a_binario(numero1_decimal)
            numero2_binario = decimal_a_binario(numero2_decimal)

            # Escribir la línea de números binarios en el archivo de salida
            linea_binaria = f"{numero1_binario};{numero2_binario}\n"
            f_out.write(linea_binaria)

# Nombres de archivos de entrada y salida para números positivos y negativos
archivo_entrada_positivos = "PositivosP.txt"
archivo_salida_positivos_binario = "PositivosP_binario.txt"

archivo_entrada_negativos = "NegativosP.txt"
archivo_salida_negativos_binario = "NegativosP_binario.txt"

# Procesar archivos de entrada y escribir resultados en archivos de salida
procesar_archivo(archivo_entrada_positivos, archivo_salida_positivos_binario)
procesar_archivo(archivo_entrada_negativos, archivo_salida_negativos_binario)
