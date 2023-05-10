class Shop:
    '''класс магазин в котором выполняются операции покупки'''
    def __new__(cls, id, name, price, amound):
        '''создаем экземпляр класс Shop'''
        if not hasattr(cls, 'shop'):
            cls.shop = super(Shop, cls).__new__(cls)
        return cls.shop

    def shop_operation(self):
        '''Основные действия по покупке'''
        if self.amound > 0:
            if self.name in person_1.list_product:#проверяем есть ли товар в списке покупок и колличество его на прилавке
                print(f"Количество товара в наличии перед тем как взяли {self.name} - {self.amound}")#выводим количество товаров до того как положили в корзину
                shopping_basket.sum_product += self.price # общая сумма покупки
                if shopping_basket.sum_product < person_1.money:# проверяем общую сумму с деньгами покупателя
                    # если общей суммы хватает то добавляем в карзину товар
                    person_1.basket.append(self.name)
                    self.amound -= 1
                else:
                    print("На данный товар не достаточно средств")
                print(f"Количество товара в наличии после того как взяли {self.name} - {self.amound}")  # выводим количество товаров после того как положили в корзину
            else:
                print(f"Продукт {product_1.name} отсутствует в списке покупок")
        else:
            print(f"Продукт {product_1.name} отсутствует на полках магазина")
        return person_1.basket


class Product(Shop):
    '''product in shop'''
    def __init__(self, id, name, price, amound):
        self.id = id
        self.name = name
        self.price = price
        self.amound = amound

class Buyer:
    '''Класс покупатель'''
    def __init__(self, id, money, list_product, basket = None):
        self.id = id
        self.money = money
        self.list_product = list_product
        self.basket = []
    @classmethod
    def add_basket(cls, id, money, list_product, basket):
        return cls(id, money, list_product, basket)

class shopping_basket:
    sum_product = 0 #общая сумма покупок
    def basket(self):
        #вывод того что было куплено и оставшихся средст
        person_1.money = person_1.money - shopping_basket.sum_product
        if person_1.money >= 0:
            print(f"Были купленны следующие товары: {person_1.basket}, на вашем счету осталось {person_1.money}")
        else:
            print("На вашем счету не достаточно средств")

    def new_list_product(self):
        # вывод того что не было купленно из списка покупок
        for elem_product_basket in person_1.basket:
            for elem_product in person_1.list_product:
                if elem_product == elem_product_basket:
                    person_1.list_product.remove(elem_product)
        return person_1.list_product


person_1 = Buyer(1, 100, ["milk", "cola", "bread"])
person_1 = person_1.add_basket(1, 10, ["milk", "cola", "kefir"], ['Пустая корзина'])
product_1 = Product(1, "milk", 1.99, 30)
product_1.shop_operation()
product_2 = Product(2, "cola", 2.09, 121)
product_1.shop_operation()
product_3 = Product(3, "bread", 0.99, 0)
product_1.shop_operation()
product_4 = Product(4, "cat eat", 4.99, 30)
product_1.shop_operation()
basket = shopping_basket()
basket.basket()
print(f"Данных продуктов не было в наличии {basket.new_list_product()}")
