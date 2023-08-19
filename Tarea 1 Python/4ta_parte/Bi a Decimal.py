def binario_a_decimal(binario):
    # Divide el número binario en partes enteras y fraccionarias
    partes = binario.split('.')
    parte_entera = int(partes[0], 2)  # Convierte la parte entera binaria a decimal
    parte_fraccionaria = 0.0
    
    if len(partes) > 1:
        # Convierte la parte fraccionaria binaria a decimal utilizando la fórmula de la suma ponderada
        parte_fraccionaria = sum(int(bit) * 2**(-i - 1) for i, bit in enumerate(partes[1]))
    
    numero_decimal = parte_entera + parte_fraccionaria
    return round(numero_decimal, 3)  # Redondea el número decimal a 3 decimales

def procesar_archivo_binario(archivo_entrada, archivo_salida, negativos=False):
    # Abre archivos de entrada y salida en sus respectivos modos
    with open(archivo_entrada, 'r') as f_in, open(archivo_salida, 'w') as f_out:
        for linea in f_in:
            numero_binario = linea.strip()
            numero_decimal = binario_a_decimal(numero_binario)
            
            if negativos:
                numero_decimal = -numero_decimal  # Si se especifica, convierte el número decimal a negativo
            
            # Escribe el número decimal en el archivo de salida y muestra un mensaje en la consola
            f_out.write(f"{numero_decimal}\n")

# Nombres de archivos de entrada y salida para números positivos y negativos
archivo_entrada_suma_positivos = "SumaP.txt"
archivo_salida_positivos = "Positivos.txt"

archivo_entrada_suma_negativos = "SumaN.txt"
archivo_salida_negativos = "Negativos.txt"

# Procesar archivos de entrada y escribir resultados en archivos de salida
procesar_archivo_binario(archivo_entrada_suma_positivos, archivo_salida_positivos)
procesar_archivo_binario(archivo_entrada_suma_negativos, archivo_salida_negativos, negativos=True)
