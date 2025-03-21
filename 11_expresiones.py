"""
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""

def balanced_signs(expresion: str) -> bool:

    #Los arrays de los diferentes caracteres de apertura y cierre de las expresiones.
    char_start = ['{', '[', '(']
    char_finish = ['}', ']', ')']

    #Creo un array con los caracteres a evaluar
    fixed = [char for char in expresion if char in char_start + char_finish]

    stack = []

    for char in fixed:
        if char in char_start:
            stack.append(char_finish[char_start.index(char)])
        else:
            if not stack or stack.pop() != char:
                print(f'La expresión {expresion} NO esta balanceada')
                return False
            
    is_balanced = len(stack) == 0

    if is_balanced:
        print(f'La expresión {expresion} esta balanceada!!!')
        return is_balanced
    else:
        print(f'La expresión {expresion} NO esta balanceada')
        return False

if __name__ == "__main__":
    txt = '() [ ]{ [ ( ) ] }'
    r = balanced_signs(txt)
    print(r)