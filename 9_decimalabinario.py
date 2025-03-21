"""
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

import math 

def decimalToBinary(num: int):

    c_num = num
    binary = ""
    f_binary = ""

    while num > 0:
        mod = str(num % 2)
        num = math.floor(num / 2)
        binary = binary + mod

    for i in range(1, len(binary)+1):
        f_binary = f_binary + binary[len(binary)-i]

    f_binary = int(f_binary)

    print(f"El número {c_num} en binario es: {f_binary}")

if __name__ == "__main__":
    number = 23519
    decimalToBinary(number)