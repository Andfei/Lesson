from dataclasses import dataclass
from typing import Optional
import csv
'''
Task_9 Lesson_1
'''
class Car:
    '''Описание модели'''
    def __init__(self, model):
        '''свойства модели'''
        self.model = model
        if self.model == "BMW":
            self.age = 12
            self.color = "red"
            self.weight = 240
            print(f"| 1 | {model} | {self.age} | {self.color} | {self.weight} |")
        elif self.model == "Audi":
            self.age = None
            self.color = "Black"
            self.weight = 120
            print(f"| 2 | {model} | {self.age} | {self.color} | {self.weight} |")

    def move(self):
        '''выводит сообщение MOVE'''
        print("Move")

    def stop(self):
        '''выводит сообщение Stop'''
        print("Stop")

    def birthday(self, age):
        '''Прибовляет к возрасту 1 год'''
        try:
            self.age += 1
            return self.age
        except:
            return "атрибут age не задан"

print("____" * 12)
car_1 = Car(model = "BMW")
car_1.stop()
car_1.move()
print(f"New_age: {car_1.birthday(car_1.age)}")
print("____" * 12)
car_2 = Car(model = "Audi")
car_2.stop()
car_2.move()
print(f"New_age: {car_2.birthday(car_2.age)}")
print("____" * 12)
'''
Task_9 Lesson_2 
'''
@dataclass
class Person:
    '''свойства модели'''
    name: str
    age: Optional[int]

    @property
    def birth_year(self):
        '''считает год рождения'''
        return 2023 - self.age


with open("tASK_9.csv", encoding='utf-8') as r_file:
    '''читаем файл'''
    file_reader = csv.reader(r_file, delimiter = ",")
    for row in file_reader:
        '''проходимся по элементам файла'''
        age = int(row[1])
        name = row[0]
        person = Person(name, age)
        '''выводим имя и год рождения '''
        print(f"Имя:{person.name} Год рождения: {person.birth_year}")


