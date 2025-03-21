"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci(c: int):
    a1 = 0
    a2 = 1
    f = 0

    for i in range(0, c):
        if i == 0:
            print(a1)
        elif i == 1:
            print(a2)
        else:
            f = a1 + a2
            a1 = a2
            a2 = f
            print(f)

if __name__ == "__main__":
    c = int(input("¿Cuantos números de la suceción de fibonacci desea ver?"))
    fibonacci(c)
