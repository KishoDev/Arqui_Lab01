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
                    # Abre el archivo 'positivosP.txt' en modo adición ('a') y escribe la línea
                    with open('positivosP.txt', 'a') as pos_file:
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
