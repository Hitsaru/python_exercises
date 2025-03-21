"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

def validar_primos(n: int):

    count_n = 0
    for w in range(1, n + 1):
        if (n % w) == 0:
            count_n += 1

    if count_n == 2: 
        print(f"El número {n} es primo!")
    else: 
        print(f"El número {n} no es primo!")

    for i in range(1, 101):
        count = 0
        for j in range(1, i + 1):
            if (i % j) == 0:
                count = count + 1
            
        if count == 2:
            print(i)




if __name__ == "__main__":
    n = 17
    validar_primos(n)
