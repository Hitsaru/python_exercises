"""
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
"""

def factorial(v_factorial: int) -> int:

    if v_factorial > 0:
        result = v_factorial * factorial(v_factorial - 1)
        return result
    else: 
        return 1

if __name__ == '__main__':
    n = 10
    r = factorial(n)
    print(f'!{n} = {r}')

