"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""

def ver_anagrama(a: str, b: str):

    if a == b:
        return False
    
    new_a = sorted(a)
    new_b = sorted(b)

    if new_a == new_b: 
        return True
    else:
        return False

if __name__ == "__main__":
    a = "holaa"
    b = "ahol"
    r = ver_anagrama(a,b)
    print(r)