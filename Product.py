import random


class Product:
    """Класс для описания товара"""

    def __init__(
            self, name: str='NA', code: int=None,
            count: int=0)-> None:
        """Инициализатор класса.

        Args:
            name: Наименование товара
            code: Шифр товара
            count: Количество товара
        """

        self.__name = name
        if code is None:
            self.__code = random.randrange(1, 10 ** 3)
        else:
            self.__code = code
        self.__count = count

    def get_name(self):
        """Геттер для наименования товара.

        Returns:
                name: Наименование товара
        """

        return self.__name

    def get_code(self):
        """Геттер для шифра товара.

        Returns:
                code: Шифр товара
        """

        return self.__code

    def get_count(self):
        """Геттер для количества товара.

        Returns:
                count: Количество товара
        """

        return self.__count

    def set_name(self, name: str):
        """ Сеттер для названия товара

            Args:
                name: Наименование товара
        """

        if len(name) == 0:
            print("Введите наименование товара,используя буквы")
        else:
            self.__name = name

    def set_count(self, count: int = 0):
        """ Сеттер для количества товара

            Args:
                count: Количество товара
        """

        if count < 0:
            print('Введите положительное число')
        else:
            self.__count = count

    def set_code(self, code: int = None) -> None:
        """ Сеттер для шифра товара

            Args:
                code: Шифр товара
        """

        if code is None:
            self.__code = random.randrange(1, 10 ** 3)
        else:
            self.__code = code

    def display_information(self) -> None:
        """Вывод информации о товаре."""

        print(
        f'\nНаименование: {self.get_name()}\n'
        f'Шифр:{self.get_code()}\n'
        f'Количество:{self.get_count()}\n'
        )


    def add_count(self, add: int = None)-> None:
        """Добавить количество товара.

        Args:
            add: Число, на сколько нужно увеличить количество товара.
        """

        if add > 0:
            new_count = self.get_count() + add
            self.set_count(new_count)
            print(f'Количество товара {self.get_name()}={self.get_count()} ')
        else:
            print('Введено некорректное число')

    def down_count(self, meaning: int)-> None:
        """Уменьшить количество товара.

        Args:
            meaning: Число, на сколько нужно уменьшить количество товара.
        """

        if meaning > 0:
            new_count = self.get_count() - meaning
            self.set_count(new_count)
            print(f'Количество товара {self.get_name()} = {self.get_count()} ')
        else:
            print('Введено некорректное число')

    def avialability_product(self)-> None:
        """Проверить наличие товара."""

        if self.get_count() > 0:
            print(f'Осталось в наличии {self.get_count()} штук')
        else:
            print('Товара нет в наличии')


