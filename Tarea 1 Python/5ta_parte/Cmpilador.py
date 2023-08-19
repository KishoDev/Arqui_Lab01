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
