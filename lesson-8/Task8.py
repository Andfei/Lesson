import json
import csv
'''
Работа с исключениями
'''
'''
Задание 1
'''
dict_ = {0: 0, 1: 2, 3: 4}


def funk(dict_, key):
    try:
        return dict_[key]
    except:
        return None


print(funk(dict_, 5))
print(funk(dict_, 0))
'''
   Работа с файлами 
'''
'''
Задание 1
'''
str1 = input("Input string 1:")
str2 = input("Input string 2:")
str3 = input("Input string 3:")
str4 = input("Input string 4:")

file = open("String.txt", "w+")
file.write(str1 + '\n')
file.write(str2 + '\n')
file.close()

with open("String.txt") as f:
    print(f.read())

file = open("String.txt", "a")
file.write(str3 + '\n')
file.write(str4 + '\n')
file.close()
'''
Задание 2
'''
data = {
    666666: ("Andry", 22),
    666665: ("Andry", 23),
    666664: ("Andry", 24),
    666663: ("Andry", 25),
    666662: ("Andry", 26),
}

with open("data_file_3.json", "w") as write_file:
    json.dump(data, write_file)
'''
Задание 3
'''
with open("data_file_3.json", "r") as read_file:
    data = json.load(read_file)
print(data)

new_dict = []
for key in data:
    new_dict.append(data[key])
new_dict.insert(0, ("name", "Age", "phone"))


with open('sw_data.csv', 'w+') as f:
    writer = csv.writer(f)
    for row in new_dict:
        writer.writerow(row)

with open('sw_data.csv') as f:
    print(f.read())






