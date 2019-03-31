import shutil
import sys

NAMEMENU = {'main':'Добро пожаловать в адресную книгу ntone!','submenu':'='*40}
MAINMENU = ['Войти в телефонную книгу', 'Войти в каталог сайтов', 'Настройки', 'Выход']
TELMENU = ['Просмотреть всю книгу', 'Добавить контакт', 'Редактировать контакт', 'Выход']
SITEMENU = ['Просмотреть всю книгу', 'Добавить сайт', 'Редактировать сайт', 'Выход']
PREFMENU = ['Здесь пока ничего нет']
EXITMENU = ['Выход']
COMMANDPACK = [MAINMENU, TELMENU, SITEMENU, PREFMENU, EXITMENU]
EXITPOSITION = '4'

class Menu(object):
    terminal_window = shutil.get_terminal_size((80,20)) 
    SEPARATOR = '=' * terminal_window.columns
    WELCOME = '\n' * terminal_window.lines + int(terminal_window.columns / 2 - 20) * '=' + '{namemenu}' + int(terminal_window.columns / 2 - 20) * '='
    
    def choicecommand(self, commandpack):
        while True:
            current_command = input('Введите номер команды: ')
            print(current_command)
            # if current_command == '4': 
            #     print('exit')
            #     break
            for position in range(len(commandpack)):
                if current_command == str(position + 1):
                    submenu = Menu(NAMEMENU['submenu'], commandpack, position) 
            
            print('Введена некорректная команда')

    def __init__(self, namemenu, commandpack, idmenu):
        self.commandpack = commandpack
        self.namemenu = namemenu
        self.welcome = Menu.WELCOME.format(namemenu = self.namemenu)
        self.show_menu(self.welcome, commandpack[idmenu])
        self.choicecommand(commandpack)
    
    def show_menu(self, welcome, commandlist):
        print(self.SEPARATOR)
        print(self.welcome)
        for i in range(1,len(commandlist)+1):
            print('{n}. {command}'.format(n = i, command = commandlist[i - 1]))

mainmenu = Menu(NAMEMENU['main'], COMMANDPACK, 0)

