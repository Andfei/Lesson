'''генератор от 0 до бесконечности'''
def count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step



count = count()
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))

'''Итератор от 0 до задонного числа'''
class HelloIterator:

    def __init__(self, num_iters):
        self.num_iters = num_iters
        self.counter = 0

    def __iter__(self):
        return self  # возвращаем self тк HelloIterator уже будет ябляться итератором

    def __next__(self):
        if self.counter < self.num_iters:
            self.counter += 1
            return self.counter - 1
        raise StopIteration

number = int(input("Imput number iter:"))
for item in HelloIterator(number):
    print(item)
print(number)
'''дописать класс Family'''


class Family:

    def __init__(self, id, last_name, members):
        self.id = id
        self.last_name = last_name
        self.members = members
        self.counter = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.members):
            self.counter += 1
            return self.members[self.counter - 1]
        raise StopIteration

    def __len__(self):
        return len(self.members)

    def add_family_member(self, member):
        self.members.append(member)

    def __str__(self):
        return f"Family: last_name - {self.last_name}, count - {len(self.members)}"

    def id_number(self, id):
        self.id-=1
        return self.members[self.id]



class FamilyMember:

    def __init__(self, id, name, role=None, age=None):
        self.id = id
        self.name = name
        self.role = role
        self.age = age

    def __str__(self):
        return f"FamilyMember: {self.name}, role: {self.role}"


son = FamilyMember(id=1, name="Roma", role="son")
father = FamilyMember(id=2, name="Nikita", role="father", age=43)
id_ = int(input("Person id:"))
members = [son, father]
family = Family(id=id_, last_name="Гаврильчик", members=members)

for ite in family:
    print(ite)

print(family.id_number(id))
'''числа фибоначчи'''
def get_num_list(num, a, b):
    numbers = []
    for i in range(num):
        a, b = b, a + b
        numbers.append(a)
    return numbers

number = int(input("Input namber "))
print(get_num_list(number, 0, 1))