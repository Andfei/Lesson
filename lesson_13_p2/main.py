import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

URL = "https://jsonplaceholder.typicode.com/todos"

class Todo:

    def __init__(self, id, response):
        self.response = response
        self.id = id
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.response):
            self.counter += 1
            return self.response[self.counter - 1]
        raise StopIteration

    def Id_(self): # поиск по id
        for self.counter in range(len(self.response)):
            if self.response[self.counter-1]['id'] == self.id:
                return self.response[self.id - 1]['id']

    def record_file(self):# запись в json файл
        with open("data_file_1.json", "w") as write_file:
            json.dump(self.response, write_file)

    def read_file(self):# чтение из json файла
        with open('data_file_1.json') as json_file:
            data = json.load(json_file)
            for p in data:
                print(f'userId: {p["userId"]} id: {p["id"]} title: {p["title"]} completed: {p["completed"]}')


response_ = requests.get(os.environ.get("URL"))
response_ = response_.json()
# выводим данные
for item in Todo(id=None, response=response_):
    print(item)
# id который нам нужен
id = int(input("Imput number iter:"))
todo = Todo(id=id, response=response_)
print(todo.Id_())
todo.record_file()
todo.read_file()
