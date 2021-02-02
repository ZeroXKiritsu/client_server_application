'''
Задание №3:
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе.
'''

var = b'attribute'
var2 = b'класс'
var3 = b'функция'
var4 = b'type'

print(var, var2, var3, var4)

'''
Итог:
File "C:\Users\kalen\Desktop\client_server_application\attribute.py", line 8
    var2 = b'класс'
                        ^
SyntaxError: bytes can only contain ASCII literal characters.

итог: строки записанные на кириллице  невозможно записать в байтовом типе
'''