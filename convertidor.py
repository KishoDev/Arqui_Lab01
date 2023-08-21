from os import remove

#-----------------------------------------------------------------------------------------------------------------------------------------#
'''
NOMBRE : integer_to_binary(number)
***
INPUT 
    number : int
***
FUNCION:
    Transforma un entero dado a binario
'''
def integer_to_binary(number):
    binary = ''

    while number >= 1:
        binary = str(number % 2) + binary
        number //= 2
    
    return binary


#-----------------------------------------------------------------------------------------------------------------------------------------#
'''
NOMBRE : binary_to_integer(binary)
***
INPUT 
    binary : int
***
FUNCION:
    Tranforma un binario dado a entero.
'''
def binary_to_integer(binary):
    binary = str(binary)
    output = 0
    i = len(binary) - 1
    while i >= 0:
        if binary[-(i + 1)] == '1': output += 2**i
        i -= 1
    return int(output)


#-----------------------------------------------------------------------------------------------------------------------------------------#
'''
NOMBRE : separar_archivos(input_file)
***
INPUT 
    input_file : string
***
FUNCION:
    Lee el archivo de entrada.
'''
def separar_archivos(input_file):
    # Abre el archivo de entrada en modo lectura ('r')
    with open(input_file, 'r') as f:
        # Itera sobre cada línea en el archivo
        for line in f:
            # Divide la línea en una lista de números utilizando ';' como separador
            numeros = line.strip().split(';')
            
            # Verifica si hay exactamente dos números en la lista
            if len(numeros) == 2:
                # Comprueba si ambos números no contienen un signo negativo '-'
                if '-' not in numeros[0] and '-' not in numeros[1]:
                    # Abre el archivo 'PositivosP.txt' en modo adición ('a') y escribe la línea
                    with open('PositivosP.txt', 'a') as pos_file:
                        pos_file.write(line)
                # Comprueba si ambos números tienen un signo negativo '-'
                elif '-' in numeros[0] and '-' in numeros[1]:
                    # Elimina los signos negativos de los números y abre 'NegativosP.txt' en modo adición ('a')
                    numeros[0] = numeros[0].replace('-', '')
                    numeros[1] = numeros[1].replace('-', '')
                    with open('NegativosP.txt', 'a') as neg_file:
                        # Escribe los números modificados en formato de texto separados por ';' y agrega una nueva línea
                        neg_file.write(';'.join(numeros) + '\n')
                else:
                    # Si uno de los números es positivo y el otro negativo, abre 'inviable.txt' en modo adición ('a')
                    with open('inviable.txt', 'a') as inviable_file:
                        inviable_file.write(line)

# Llamamos a la función separar_archivos con el nombre del archivo de entrada 'operaciones.txt'
separar_archivos('operaciones.txt')


#-----------------------------------------------------------------------------------------------------------------------------------------#
'''
NOMBRE : decimal_a_binario(numero_decimal)
***
INPUT
    numero_decimal : float
***
FUNCION:
    transforma un número decimal a binario.
'''
def decimal_a_binario(numero_decimal):
    # Separar la parte entera y la parte fraccionaria del número decimal
    parte_entera = int(numero_decimal)
    parte_fraccionaria = numero_decimal - parte_entera

    # Convertir la parte entera a binario
    parte_entera_binaria = integer_to_binary(parte_entera) 

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


#-----------------------------------------------------------------------------------------------------------------------------------------#
'''
NOMBRE : procesar_archivo(archivo_entrada, archivo_salida)
***
INPUT 
    archivo_entrada : string
    archivo_salida  : string
***
FUNCION: 
    Transcribe los numeros a un nuevo archivo de texto
'''
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


#-----------------------------------------------------------------------------------------------------------------------------------------#
'''
NOMBRE : suma_binaria(binario1, binario2)
***
INPUT 
    binario1 : int
    binario2 : int
***
FUNCION:
    Suma los binarios.
'''
def suma_binaria(binario1, binario2):
    # Dividir los números binarios en partes enteras y fraccionarias
    parte_entera_binaria1, parte_fraccionaria_binaria1 = binario1.split('.')
    parte_entera_binaria2, parte_fraccionaria_binaria2 = binario2.split('.')

    # Suma de las partes enteras
    suma_parte_entera = integer_to_binary(binary_to_integer(parte_entera_binaria1) + binary_to_integer(parte_entera_binaria2))

    # Asegurar que las partes fraccionarias tengan la misma longitud
    max_len = max(len(parte_fraccionaria_binaria1), len(parte_fraccionaria_binaria2))
    parte_fraccionaria_binaria1 = parte_fraccionaria_binaria1.ljust(max_len, '0')
    parte_fraccionaria_binaria2 = parte_fraccionaria_binaria2.ljust(max_len, '0')

    # Suma de las partes fraccionarias
    if parte_fraccionaria_binaria1 and parte_fraccionaria_binaria2:  # Solo si ambas partes fraccionarias no están vacías
        suma_parte_fraccionaria = integer_to_binary(binary_to_integer(parte_fraccionaria_binaria1) + binary_to_integer(parte_fraccionaria_binaria2))
    else:
        suma_parte_fraccionaria = parte_fraccionaria_binaria1 or parte_fraccionaria_binaria2

    # Si hay acarreo en la parte fraccionaria, ajustar la parte entera
    if len(suma_parte_fraccionaria) > max_len:
        suma_parte_entera = integer_to_binary(binary_to_integer(suma_parte_entera) + 1)
        suma_parte_fraccionaria = suma_parte_fraccionaria[1:]

    # Combinar las partes enteras y fraccionarias para formar el número binario de suma
    suma_binaria = suma_parte_entera + '.' + suma_parte_fraccionaria
    return suma_binaria


#-----------------------------------------------------------------------------------------------------------------------------------------#
'''
NOMBRE : procesar_archivo_suma(archivo_entrada, archivo_salida)
***
INPUT 
    archivo_entrada : string 
    archivo_salida  : string
***
FUNCION:
    Lee los archivos de números positivos y negativos para sumarlos y los resultados los guarda en otro archivo.
'''
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
archivo_salida_suma_positivos = "SumaP.txt"

archivo_entrada_negativos = "NegativosP_binario.txt"
archivo_salida_suma_negativos = "SumaN.txt"

# Procesar archivos de entrada y escribir resultados de suma en archivos de salida
procesar_archivo_suma(archivo_entrada_positivos, archivo_salida_suma_positivos)
procesar_archivo_suma(archivo_entrada_negativos, archivo_salida_suma_negativos)

#-----------------------------------------------------------------------------------------------------------------------------------------#
'''
NOMBRE : binario_a_decimal(binario)
***
INPUT 
    binario : string
***
FUNCION:
    transforma el número binario a decimal.
'''
def binario_a_decimal(binario):
    # Divide el número binario en partes enteras y fraccionarias
    partes = binario.split('.')
    parte_entera = binary_to_integer(partes[0])  # Convierte la parte entera binaria a decimal
    parte_fraccionaria = 0.0
    
    if len(partes) > 1:
        # Convierte la parte fraccionaria binaria a decimal utilizando la fórmula de la suma ponderada
        parte_fraccionaria = sum(int(bit) * 2**(-i - 1) for i, bit in enumerate(partes[1]))
    
    numero_decimal = parte_entera + parte_fraccionaria
    return round(numero_decimal, 3)  # Redondea el número decimal a 3 decimales


#-----------------------------------------------------------------------------------------------------------------------------------------#
'''
NOMBRE : procesar_archivo_binario(archivo_entrada, archivo_salida, negativos=False)
***
INPUT 
    archivo_entrada : string
    archivo_salida  : string
    negativos       : bool. False como predeterminado.
***
FUNCION:
    Procesa los archivos auxiliares de binarios.
'''
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

#-----------------------------------------------------------------------------------------------------------------------------------------#
'''
NOMBRE : combine_files(input_files, output_file)
***
INPUT 
    input_files : string
    output_file : string
***
FUNCION:
    Toma todos los archivos txt creados en el codigo y los une en uno solo "preparado.txt"
'''
def combine_files(input_files, output_file):
    try:
        # Abre el archivo de salida en modo escritura ('w')
        with open(output_file, 'w') as output:
            # Itera sobre cada nombre de archivo en la lista de archivos de entrada
            for file_name in input_files:
                # Abre cada archivo de entrada en modo lectura ('r')
                with open(file_name, 'r') as file:
                    # Escribe el contenido del archivo en el archivo de salida, agregando una nueva línea
                    output.write(file.read() + '\n')
    except Exception as e:
        # Captura cualquier excepción que ocurra durante el proceso y muestra un mensaje de error
        print("Error:", str(e))

# Nombres de archivos de entrada y archivo de salida
input_files = ["Positivos.txt", "Negativos.txt", "inviable.txt"]
output_file = "preparado.txt"

# Llama a la función para combinar los archivos de entrada y guardar el resultado en el archivo de salida
combine_files(input_files, output_file)

#-----------------------------------------------------------------------------------------------------------------------------------------#
'''
NOMBRE : decimal_a_bin_ieee754(numero)
***
INPUT 
    numero : int ???????
***
FUNCION:
    Transforma el decimal a binario punto flotante 32 bits.
'''
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

    exponente_bits = integer_to_binary(exponente)  # Convierte el exponente en 8 bits binarios

    mantisa = ""
    for _ in range(23):
        fraccion *= 2
        bit = int(fraccion)
        mantisa += str(bit)
        fraccion -= bit

    # Combina los bits del signo, exponente y mantisa para formar la representación binaria
    representacion_binaria = signo + exponente_bits + mantisa
    return representacion_binaria


#-----------------------------------------------------------------------------------------------------------------------------------------#
'''
NOMBRE : delete_aux_files()
***
FUNCION:
    Elimina todos los archivos auxiliares.
'''
def delete_aux_files():
    remove('inviable.txt')
    remove('Negativos.txt')
    remove('NegativosP_binario.txt')
    remove('NegativosP.txt')
    remove('Positivos.txt')
    remove('PositivosP.txt')
    remove('PositivosP_binario.txt')
    remove('preparado.txt')
    remove('SumaN.txt')
    remove('SumaP.txt')
    return

#-------------------------------------------------------# MAIN STUFF #---------------------------------------------------------------------------------#
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
print("Sumas sin realizarse:", no_se_pudo)
print("Sumas realizadas:", si_se_pudo)

# Elimina todos los archivos de ayuda.
delete_aux_files()
