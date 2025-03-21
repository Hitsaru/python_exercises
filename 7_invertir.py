"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invert_string(string):
    try:
        inverted = ""
        print(f"String to invert is: {string}\n\n")
        for i in range(1, len(string)+1):
            inverted = inverted + string[len(string)-i]
        print(f"The string inverted is: {inverted}")
    except Exception:
        print("Invalid argument please give a correct string")

if __name__ == "__main__":
    word = "Hello world!"
    invert_string(word)