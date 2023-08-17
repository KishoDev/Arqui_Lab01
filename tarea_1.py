# file_in = open('operaciones.txt')
file_out = open('resultados.txt', 'w')
numeros_a_sumar, resultados = [[],[]], [[],[]]
pos, neg, i = 0, 0, 0
from math import trunc

def float_to_binary(number):
    binary = ''
    i = 0
    decimal_digits = str(number)

    while number != 0 and i >= len(decimal_digits[2:]):
        number *= 2
        binary += str(int(number))
        if number >= 1:
            number -= 1
        i += 1
    
    return binary

# Se pasa por parámetro un int.
def integer_to_binary(number):
    binary = ''

    while number >= 1:
        binary = str(number % 2) + binary
        number //= 2
    
    return binary

# Se pasa un float por parámetro
def transform_to_IEEE754(number):
    binary, signo = '', ''
    i = 0
    integer = abs(int(number))
    decimal = float(str(number)[str(number).find('.'):])

    print(integer, decimal)

    S = '1' if number < 0 else '0'
    
    binary += integer_to_binary(integer) + '.' + float_to_binary(decimal)
    
    # Convierte el número a formato notación científica. 
    E = int(str('{:e}'.format(float(binary)))[-2:]) + 127
    E = integer_to_binary(E)

    M = integer_to_binary(integer)[1:] + float_to_binary(decimal)
    
    output = S + E + M
    while len(output) > 32:
        output += '0'

    return output

def transform_to_decimal(binary):
    output = ''
    return output

def binary_addition(n1, n2):
    i = -1
    aux = 0
    output = ''

    while i > -len(n1):
        digit = int(n1[i]) + int(n2[i]) + aux
        if aux == 1: aux -= 1
        if digit > 1:
            digit -= 2
            aux += 1
        output = str(digit) + output
        i -= 1

    output = n1[-32] + output

    return output

def function(n1, n2):
    n1 = transform_to_IEEE754(n1)
    n2 = transform_to_IEEE754(n2)
    binary_result = binary_addition(n1, n2)
    number_result = transform_to_decimal(binary_result)

with open('operaciones.txt') as file_in:
    for line in file_in:
        line = line.strip()
        punto_coma = line.find(';')
        numeros_a_sumar[0].append(line[:punto_coma])
        numeros_a_sumar[1].append(line[(punto_coma + 1):])

for n1, n2 in zip(numeros_a_sumar[0], numeros_a_sumar[1]):
    print(n1, n2)
    result_normal, result_bin = funcion(n1, n2)


'''
for line in file_in:
    print(line)
    if 
    numeros_a_sumar.clear()
    line.find(';')
'''


    
# file_in.close()
file_out.close()
