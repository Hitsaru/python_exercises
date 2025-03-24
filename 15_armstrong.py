"""
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
"""

def armstrong(num: int) -> bool:

    try: 

        if num < 0:
            print(f"El número {num} NO es Armstrong (los números negativos no son válidos).")
            return False

        final_sum = 0
        str_num = str(num)
        len_num = len(str_num)
        lst_num = [number for number in str_num]

        lst_num = map(lambda x: pow(int(x), len_num), lst_num)

        for i in lst_num:
            final_sum += i
        
        isArmstrong = final_sum == num

        if isArmstrong:
            print(f'El número {num} es Armstrong, ya que {num} es igual a {final_sum}!')
            return True
        else:
            print(f'El número {num} NO es Armstrong, ya que {num} NO es igual a {final_sum}!')
            return False
    
    except Exception:
        print('We had a issue trying to solve the problem, please check the input!')
        return False
    
    
if __name__ == '__main__':

    num = 153
    armstrong(num)