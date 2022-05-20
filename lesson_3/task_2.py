"""
2. Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""


def check_number(str_number):
    try:
        number = float(str_number)

        if int(number) == number:
            return f'{str_number} - число целое'
        else:
            result = [f'{str_number} - число дробное, ']
            left, right = str_number.split('.')
            if left == right: 
                result.append('\nЛевая и правая части совпадают')
                # return True
            else: 
                result.append('\nЛевая и правая части не совпадают')
                # return False
            return ''.join(result)
    except ValueError:
        return(f'{str_number} - не число')


print(check_number(input('Введите число: ')))