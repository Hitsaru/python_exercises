"""
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
"""

def palindromo(txt: str):

    txt = txt.lower()
    lst_abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    txt_fixed = [i for i in txt if i in lst_abc]

    lst_f = txt_fixed[::-1]

    print(txt_fixed)

    print(f'Inicial: {txt_fixed}')
    print(f'Final: {lst_f}')

    if txt_fixed == lst_f:
        return True
    else:
        return False

if __name__ == '__main__':
    text = 'No soy palindromo'
    r = palindromo(text)
    print(r)