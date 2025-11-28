from Product import (
    Product,
)


class Menu:
    """Класс для работы пользовательского меню."""

    def show_menu(self) -> None:
        """Вывод пользовательского меню."""

        print(f"""
            Выберите задачу:
            1:  ПРОСМОТРЕТЬ ИНФОРМАЦИЮ ПО ТОВАРУ.
            2:  УВЕЛИЧИТЬ КОЛИЧЕСТВО ТОВАРА.
            3:  УМЕНЬШИТЬ КОЛИЧЕСТВО ТОВАРА.
            4:  ПРОВЕРИТЬ НАЛИЧИЕ ТОВАРА.
            5:  ВЫХОД.
            6:  ПОЛУЧИТЬ ИНФОРМАЦИЮ О НАИМЕНОВАНИИ ТОВАРА
            7:  ПОЛУЧИТЬ ИНФОРМАЦИЮ О ШИФРЕ ТОВАРА
            8:  ПОЛУЧИТЬ ИНФОРМАЦИЮ О КОЛИЧЕСТВЕ ТОВАРА
        """)

    def main_menu(self,choice: int, product: Product) -> bool:
        """Главное пользовательское меню.

        Args:
            choice: Выбор пользователя.
        """

        match choice:
            case 1:
                product.display_information()
            case 2:
                add= int(input('Введите число, на сколько нужно увеличить количество товара'))

                product.add_count(add)
            case 3:
                meaning= int(input('Введите число, на которое нужно уменьшить количество товара'))
                product.down_count(meaning)
            case 4:
                product.avialability_product()
            case 5:
                return False
            case 6:
                print(product.get_name())
            case 7:
                print(product.get_code())
            case 8:
                print(product.get_count())
            case _:
                print('Введите верное число')

        return True

