'''
Задание №6:
Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл
в формате Unicode и вывести его содержимое
'''

import locale

var = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w+') as f:
    for line in var:
        f.write(line + '\n')
    f.seek(0)

print(f)

file_coding = locale.getpreferredencoding()

with open('test_file.txt', 'r', encoding=file_coding) as f:
    for line in f:
        print(line)
    f.seek(0)