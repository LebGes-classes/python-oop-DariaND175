from Product import(
    Product,
)
from Menu import(
    Menu,
)


menu=Menu()
product1 = Product("Banana", None, 52)
product2 = Product('Grapefruit',None,47)

def run() -> None:
    """Запуск работы"""

    is_running=True

    while is_running:
        menu.show_menu()
        choice = int(input('Выберите действие'))
        choice_products= int(input('Выберите номер продукта'))
        product = product1 if choice_products == 1 else product2
        is_running = menu.main_menu(choice,product)

run()