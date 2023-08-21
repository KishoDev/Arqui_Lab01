Integrantes:

Nombre: Vicente Jorquera Gamonal
Rol: 202173579-8
Paralelo: 201

Nombre: Vicente Galaz Rojas
Rol: 202273554-6
Paralelo: 200



Este programa se realizó con Python 3.11.3

Instrucciones:
- Tener el archivo operaciones.txt y convertidor.py dentro de la misma carpeta.
- Ejecutar convertidor.py.



Expecificaciones de los algoritmos:

integer_to_binary(number):
  ENTRADA:
    number : int
  FUNCION:
    Convierte un número entero en su representación binaria.
  SALIDA:
    str. Representa el número en binario.
-----------------------------------------------------------
binary_to_integer(binary):
  ENTRADA:
    binary : str
  FUNCION:
    Convierte un binario en su equivalente número entero.
  SALIDA:
    int. Representa el número en entero.
-----------------------------------------------------------
separar_archivos(input_file):
  ENTRADA:
    input_file      : str
  FUNCION:
    Lee un archivo de entrada y separa los números positivos y negativos en archivos separados.
  SALIDA:
    None. No devuelve ningún valor, solo divide los números en archivos.
-----------------------------------------------------------
decimal_a_binario(numero_decimal):
  ENTRADA:
    numero_decimal  : float
  FUNCION:
    Convierte un número decimal en su representación binaria.
  SALIDA:
    str. Representa el número en binario.
-----------------------------------------------------------
procesar_archivo(archivo_entrada, archivo_salida):
  ENTRADA:
    archivo_entrada : str
    archivo_salida  : str
  FUNCION:
    Lee un archivo de entrada, convierte los números decimales en binarios y escribe los resultados en un archivo de salida.
  SALIDA:
    None. No devuelve ningún valor, solo procesa los archivos.
-----------------------------------------------------------
suma_binaria(binario1, binario2):
  ENTRADA:
    binario1        : str
    binario2        : str
  FUNCION:
    Realiza la suma de dos números binarios de punto flotante.
  SALIDA:
    str. Representa el resultado de la suma en binario.
-----------------------------------------------------------
procesar_archivo_suma(archivo_entrada, archivo_salida):
  ENTRADA:
    archivo_entrada : str
    archivo_salida  : str
  FUNCION:
    Lee archivos con números binarios, suma los números y guarda los resultados en un archivo de salida.
  SALIDA:
    None. No devuelve ningún valor, solo procesa los archivos.
-----------------------------------------------------------
binario_a_decimal(binario):
  ENTRADA:
    binario         : str
  FUNCION:
    Convierte una representación binaria de punto flotante en su equivalente número decimal.
  SALIDA:
    float. Representa el número en decimal.
-----------------------------------------------------------
procesar_archivo_binario(archivo_entrada, archivo_salida, negativos=False):
  ENTRADA:
    archivo_entrada : str
    archivo_salida  : str
    negativos : bool (predeterminado: False)
  FUNCION:
    Lee archivos con números binarios, convierte los números a decimales y guarda los resultados en un archivo de salida. Opcionalmente, puede tratar los números como negativos.
  SALIDA:
    None. No devuelve ningún valor, solo procesa los archivos.
-----------------------------------------------------------
combine_files(input_files, output_file):
  ENTRADA:
    input_files     : lista de str
    output_file     : str
  FUNCION:
    Combina el contenido de varios archivos en uno solo.
  SALIDA:
    None. No devuelve ningún valor, solo combina archivos.
-----------------------------------------------------------
delete_aux_files():
  FUNCION:
    Elimina todos los archivos auxiliares generados durante el proceso.
  SALIDA:
    None. No devuelve ningún valor, solo borra archivos.



Supuesto de formato de entrada correcto:
  Se asume que las líneas en el archivo de entrada seguirán el formato específico 

  numero_decimal1;numero_decimal2

  donde cada número es un número decimal cualquiera de formato float, el que puede ser tanto positivo como negativo (ej.: 2.0, 642.3136, -31,35, etc).
  Además se asume que los números proporcionados están en el rango válido para números decimales y que no contendrán caracteres numéricos ni especiales que puedan causar errores de análisis.



Consideraciones:
  La manera en el que se guardan los resultados lo hace con un orden en particular:
    1. resultados positivos.
    2. resultados negativos.
    3. sumas no realizadas.
  Tomar en cuenta esta estructura a la hora de la correción.
 

 
        \`*-.                    
        )  _`-.                 
       .  : `. .                
       : _   '  \               
       ; *` _.   `*-._          
       `-.-'          `-.       
         ;       `       `.     
         :.       .        \    
         . \  .   :   .-'   .   
         '  `+.;  ;  '      :   
         :  '  |    ;       ;-. 
         ; '   : :`-:     _.`* ;
[bug] .*' /  .*' ; .*`- +'  `*' 
      `*-*   `*-*  `*-*'

Copyright 2023 © All rights reserved.
