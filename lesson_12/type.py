class Zoo:

    def __init__(self, id, name_zoo, list):
        self.id = id
        self.name_zoo = name_zoo
        self.list = list
        self.counter = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.list):
            self.counter += 1
            return self.list[self.counter - 1].output_animal
        raise StopIteration

    def name_len(self):#выводит название и колличество животных
        return f"Zoo: Название - {self.name_zoo}, колличество животных - {len(self.list)}"

    def get(self, id):#выводит информацию по айди
        self.id -= 1
        return self.list[self.id].output_animal

    def add_family_member(self, list):#добавляет животное в список мадакаскара
        self.list.append(list)

    def get_by_type(self, list):#выводит информацию по типу животного
        for elem in self.list:
            elem.by_type()

    def delete(self, list):# удаляет определенного животного
        self.id -= 1
        self.list.pop(self.id)

class Animal:
    def __init__(self, id, name, type, age):
        self.id = id
        self.name = name
        self.type = type
        self.age = age

    def by_type(self): # вывод животного по типу животного
        if self.type in type_n:
            print(f"Type:{self.type} Name:{self.name} age:{self.age}")

    @property
    def output_animal(self):  # вывод информации о животном
        return f"Type:{self.type} Name:{self.name} age:{self.age}"
    @classmethod
    def creat_lion(cls, name, id): # создает алекса не смог сделать без id
        return cls(id, name, type="lion", age="1")
    @classmethod
    def creat_zebra(cls, name, id): # создает марти не смог сделать без id
        return cls(id, name, type="zebra", age="6")

'''животныеиз мультика мадагаскар'''
lion = Animal.creat_lion(name="Alex", id=1)
zebra = Animal.creat_zebra(id=2, name="Marty")
hippo = Animal(id=3, name="Gloria", type="hippo", age="12")
giraffe = Animal(id=4, name="Melman Mankeyywich III", type="giraffe", age="9")
penguin_skipper = Animal(id=5, name="skipper", type="penguin", age="20")
penguin_kowalski = Animal(id=6, name="kowalski", type="penguin", age="18")
penguin_rico = Animal(id=7, name="rico", type="penguin", age="13")
penguin_private = Animal(id=8, name="private", type="penguin", age="7")

'''список животных в зоопарке'''
list_animal = [lion, zebra, hippo, giraffe]

'''пингвины которые сбежали'''
list_animal_not_zoo = [penguin_private, penguin_skipper, penguin_rico, penguin_kowalski]

'''менюшечка для удобства'''
while True:
    operation = int(input("Выберите операцию: \n 1-добавить животное \n 2-получить животное по id "
                          "\n 3-получить животное по типу \n 4-удалить животное"
                          "\n 5-название зоопарка и колличество животных в нем \n 6-список животных \n Ваш выбор:"))

    if operation == 1:# добавить животное
        madagaskar = Zoo(id=None, name_zoo="Мадакаскар", list=list_animal)
        name = int(input("Есть 4 пингвина которые сбежали кого вы хотите вернуть цифра от 1 до 4:"))
        name -= 1 # чтобы начать с 0
        madagaskar.add_family_member(list_animal_not_zoo[name])
        print(f"Добавили животное {list_animal_not_zoo[name].output_animal}")
    elif operation == 2:# получить животное по id
        id_ = int(input("Введите id животного которого хотите получить: "))
        madagaskar = Zoo(id=id_, name_zoo="Мадакаскар", list=list_animal)
        for elem in range(len(list_animal)):
            if id_ == elem: # проверяем есть ли данный айди
                print(madagaskar.get(id))
    elif operation == 3:# получить животное по типу
        madagaskar = Zoo(id=None, name_zoo="Мадакаскар", list=list_animal)
        type_n = input("Какой тип животного вам интересен")
        madagaskar.get_by_type(list_animal)
    elif operation == 4:# удалить животное
        id_ = int(input("Введите id животного которорый сбежал: "))
        madagaskar = Zoo(id=id_, name_zoo="Мадакаскар", list=list_animal)
        for elem in range(len(list_animal)):
            if id_ == elem:# проверяем есть ли данный айди
                madagaskar.delete(id)

    elif operation == 5:# название зоопарка и колличество животных в нем
        madagaskar = Zoo(id=None, name_zoo="Мадакаскар", list=list_animal)
        print(madagaskar.name_len())
    elif operation == 6: # список животных
        madagaskar = Zoo(id=None, name_zoo="Мадакаскар", list=list_animal)
        for ite in madagaskar:
            print(ite)
    else:
        print("Не верная операция введите снова")
'''
То что я знаю что не правильно сделал:
1- я объявляю в каждом if madagaskar вот 
но я уверен что можно сделать одно обьявление но если я 
перед if поставлю madagaskar = Zoo(id=None, name_zoo="Мадакаскар", list=list_animal)
то вывод по id работает криво
2- classmethod нужно было сделать с name только, но когда у меня просто имя то выбивает ошибку по __init__ 
'''



