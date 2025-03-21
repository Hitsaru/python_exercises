"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""

def area_poligono(tipo: str):

    match tipo:
        case "t":
            b = int(input("Digite la base del triangulo: "))
            h = int(input("Digite la altura del triangulo: "))

            a = (b*h)/2

            print("El área del triángulo es: ", a)
        case "c":
            l = int(input("Digite el valor de uno de los lados del cuadrado: "))

            a = l * l
            print("El área del cuadrado es: ", a)

        case "r":
            b = int(input("Digite el valor de la base del rectagulo: "))
            h = int(input("Digite el valor de la altura del rectangulo: "))

            a = b * h
            print("El área del rectangulo es: ", a)


if __name__ == "__main__":
    t = str(input("Según el área del polígono que deseas hallar digita 't' para triangulo, 'c' para cuadrado o 'r' para un rectangulo: "))
    area_poligono(t)