'''
Задание №5:
Выполнить пинг веб-ресурсов yandex.ru, youtube.com
и преобразовать результаты из байтовового в строковый тип на кириллице
'''
import subprocess

args = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for line in args:
    ping = subprocess.Popen(line, stdout=subprocess.PIPE)
    for process in ping.stdout:
        print(process)
        process = process.decode('cp866').encode('utf-8')
        print(process.decode('utf-8'))