"""
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
"""

def count_words(sentence: str):

    try: 

        signs = [",", ".", ";", ":", "!", "?", "-", "_", "(", ")", "[", "]", "{", "}", "'", '"']
        sentence = sentence.lower()
        list_count = sentence.split()
        
        for i in signs:
            list_count = list(map(lambda x: x.replace(i, ""), list_count))

        dict_words = dict()

        dict_words = dict_words.fromkeys(list_count, 0)

        for i in list_count:
            dict_words[i] = dict_words[i] + 1

        print("\nRepetión de las palabras dentro del texto proporcionado: \n")
        for i in dict_words:
            print(f"{i}: {dict_words[i]}")

    except Exception:
        print("Argument invalid, please write a correct string")



if __name__ == "__main__":
    s = "Hola como como no hay otro no hola que, ellos tomen como ellos, son no puede otro lograr eso que no toma palabra."
    count_words(s)