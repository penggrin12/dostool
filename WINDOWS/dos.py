import sys,os

def info():
        print('#      DOS TOOL')
        print('#       Build 4')
        print('#     By Penggrin')
        
def cls():
        os.system('cls')
        
cls()
info()

def info():
        print(
'''
# +-------------------------+
# |````````Дисклеймер```````|
# | ИСПОЛЬЗОВАНИЕ ПРОГРАММЫ |
# |В ПЛОХИХ ЦЕЛЯХ ЗАПРЕЩЕНО |
# +-------------------------+
''')
info()
print('# Выбери сайт')
print('# (Пример: google.com)')
site = input('* ')

if site == "":
        print('# Сайт не может быть пустым')
        exit()
        
elif site == " ":
        print('# Сайт не может быть пустым')
        exit()
        
cls()
os.system('python modules/dos.py '+site)
