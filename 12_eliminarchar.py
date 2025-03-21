""""
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
"""

def char_diferences(string1: str, string2: str):

    set1 = set(string1)
    set2 = set(string2)

    output_str1 = ''.join([char for char in string1 if char not in set2])
    output_str2 = ''.join([char for char in string2 if char not in set1])

    print(f'Texto 1: {output_str1}')
    print(f'Texto 2: {output_str2}')

if __name__ == '__main__':

    char1 = 'hola'
    char2 = 'munlo'
    char_diferences(char1, char2)    
