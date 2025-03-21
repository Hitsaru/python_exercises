"""
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
"""

lst_az = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                   'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6',
                     '7', '8', '9', '.', ',', '?', '"', '/']

lst_morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
        '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', 
        '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', 
        '--..', '-----', '.----', '..---', '...--', '....-', '.....', 
        '-....', '--...', '---..', '----.', '.-.-.-', '--..--', '..--..', '.-..-.', '-..-.']

def morseToText(txt: str):
    try:
        dict_morse = {}
        txt_converted = ''

        for i in range(0, len(lst_az)):
            dict_morse[lst_morse[i]] = lst_az[i]

        lst_txt = txt.split(' ')
        for i in lst_txt:
            if i == '':
                txt_converted = txt_converted + ' '
            if i in lst_morse:
                txt_converted = txt_converted + dict_morse[i]

        if len(txt_converted) > 0:
            print(f'El código morse: "{txt}" a texto es: "{txt_converted}"')
            return txt_converted
        else:
            print('No se ha descifrado código, porfavor verifica que el código sea valido!')

    except Exception:
        print('We had a issue prossesing the code, please verify that the code is valid')

def textToMorse(txt: str):
    try:
        dict_az = {}
        txt_converted = ''

        for i in range(0, len(lst_az)):
            dict_az[lst_az[i]] = lst_morse[i]

        for j in txt:
            if j == ' ': 
                txt_converted = txt_converted + ' '
            if j in lst_az: 
                txt_converted = txt_converted + dict_az[j] + ' '

        if len(txt_converted) > 0:
            print(f'El texto: "{txt}" a código morse es: "{txt_converted}"')
            return txt_converted
        else:
            print('No se ha descifrado ningun texto, porfavor verifica que el texto sea valido!')

    except Exception:
        print('We had a issue prossesing the text, please verify that the text is valid')

def identify_text(txt: str):
    try:
        lst_verify = ['.', '-', ' ']
        txt = txt.lower()
        isMorse = True

        for i in txt:
            if i not in lst_verify:
                isMorse = False
                break

        if isMorse:
            return morseToText(txt)
        else:
            return textToMorse(txt)

    except Exception:
        print('We had a issue prossesing the text, please verify that the text is valid')

if __name__ == '__main__':

    text = '.... --- .-.. .-'
    identify_text(text)
