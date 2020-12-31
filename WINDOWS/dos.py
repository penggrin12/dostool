import sys,os

def info():
        print('#      DOS TOOL')
        print('#       Build 2')
        print('#     By Penggrin \n')
        
def cls():
        os.system('cls')
        
cls()
info()

print('# Выбери сайт:')
site = input('# >')

if site == "":
        print('# Сайт не может быть пустым')
        cls()
        exit()
        
elif site == " ":
        print('# Сайт не может быть пустым')
        cls()
        exit()
        
os.system('clear')
os.system('python modules/dos.py '+site)
