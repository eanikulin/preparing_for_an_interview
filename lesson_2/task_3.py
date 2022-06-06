"""
4. Реализовать возможность переустановки значения цены товара.
Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса
и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар {self.name}, цена {self.price}'


item = ItemDiscountReport('Диван', 11000)
item.set_price(12000)
print(item.get_parent_data())
