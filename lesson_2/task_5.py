"""
6. Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены.
Далее реализовать выполнение каждой из функции тремя способами.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport1(ItemDiscount):
    def get_info(self):
        return self.name


class ItemDiscountReport2(ItemDiscount):
    def get_info(self):
        return self.price


item1 = ItemDiscountReport1('Диван', 11000)
print(item1.get_info())

item2 = ItemDiscountReport2('Кровать', 12000)
print(item2.get_info())

for item in (item1, item2):
    print(item.get_info())

def obj_handler(obj):
    return obj.get_info()

print(obj_handler(item1))
print(obj_handler(item2))

