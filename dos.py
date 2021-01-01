import sys,os

def info():
        print('#      DOS TOOL')
        print('#       Build 4')
        print('#     By Penggrin')
        
def cls():
        os.system('clear')
        
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
def menu():
	print('''
#	Меню:
#  	1) ДДос
#  	2) Время''')
	try:
		v = input('* ')
	except:
		print('# Фатальная ошибка')
		exit()
	
	if int(v) == 1:
		dos()
	elif int(v) == 2:
		os.system('python modules/time.py ')
	else:
		print('# Ты ввёл что-то не так')
		exit()

def dos():
        cls()
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

menu()
