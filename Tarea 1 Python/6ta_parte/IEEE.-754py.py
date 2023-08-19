def decimal_a_bin_ieee754(numero):
    # Función para convertir un número decimal en representación IEEE 754

    if numero == 0:
        return '0' * 32  # Retorna representación 32 bits de 0 si el número es cero

    if numero < 0:
        signo = '1'  # Marca el bit de signo como 1 para números negativos
        numero = -numero
    else:
        signo = '0'  # Marca el bit de signo como 0 para números positivos

    exponente = 127  # Valor del exponente en representación sesgada

    # Normaliza el número, ajustando el exponente y la fracción
    fraccion = numero
    while fraccion >= 2:
        fraccion /= 2
        exponente += 1
    while fraccion < 1:
        fraccion *= 2
        exponente -= 1
    fraccion -= 1  # Quita el bit implícito en la representación IEEE 754

    exponente_bits = format(exponente, '08b')  # Convierte el exponente en 8 bits binarios

    mantisa = ""
    for _ in range(23):
        fraccion *= 2
        bit = int(fraccion)
        mantisa += str(bit)
        fraccion -= bit

    # Combina los bits del signo, exponente y mantisa para formar la representación binaria
    representacion_binaria = signo + exponente_bits + mantisa
    return representacion_binaria

nombre_archivo_entrada = "preparado.txt"
nombre_archivo_salida = "resultado.txt"

# Abre el archivo de entrada en modo lectura y el archivo de salida en modo escritura
with open(nombre_archivo_entrada, 'r') as archivo_entrada, open(nombre_archivo_salida, 'w') as archivo_salida:
    for num_linea, linea in enumerate(archivo_entrada, start=1):
        numeros = linea.strip().split(';')

        if len(numeros) == 1:
            try:
                num = float(numeros[0])
                binario_num = decimal_a_bin_ieee754(num)
                linea_salida = f"{num}/{binario_num}\n"
                archivo_salida.write(linea_salida)
            except ValueError:
                print(f"Error al convertir la línea {num_linea}: {linea.strip()}")

        elif len(numeros) == 2:
            try:
                num1 = float(numeros[0])
                num2 = float(numeros[1])
                binario_num1 = decimal_a_bin_ieee754(num1)
                binario_num2 = decimal_a_bin_ieee754(num2)
                linea_salida = f"{num1}/{binario_num1};{num2}/{binario_num2}\n"
                archivo_salida.write(linea_salida)
            except ValueError:
                print(f"Error al convertir la línea {num_linea}: {linea.strip()}")

# Mensaje de finalización del proceso
print("Conversión completada. Valores binarios guardados en 'resultado.txt'.")
