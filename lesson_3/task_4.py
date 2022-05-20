"""
4. Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.

Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.

Вся программа должна запускаться по вызову первой функции.
"""


import os
import random
import string


LENGTH = 10


def get_random_char():
    return random.choice(string.ascii_lowercase)


def get_random_string(length):
    random_list = [get_random_char() for i in range(length)]
    return ''.join(random_list)


def create_text_file(name):
    if os.path.isfile(name):
        print('Файл с таким именем уже существует')
        return False
    with open(name, 'w', encoding='utf-8') as file:
        numbers = [random.randint(0, 100) for _ in range(LENGTH)]
        strings = [get_random_string(LENGTH) for _ in range(LENGTH)]
        file.writelines([f'{number} {text}\n' for number, text in zip(numbers, strings)])
        return file


def print_text_file(desc):
    with open(desc.name, 'r', encoding='utf-8') as read_file:
        for line in read_file:
            print(line)


descriptor = create_text_file('new_file_task4.txt')
if descriptor:
    print_text_file(descriptor)
