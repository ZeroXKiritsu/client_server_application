'''
Задание №4:
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить обратное
преобразование (используя методы encode и decode).
'''

var = ['разработка', 'администрирование', 'protocol', 'standard']

for line in var:
    str_1 = line.encode('utf-8')
    print(str_1, type(str_1))
    str_2 = bytes.decode(str_1, 'utf-8')
    print(str_2, type(str_2))