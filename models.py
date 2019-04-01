import shutil
import sys


class Menu(object):
    '''
        name - название папки в списке для отображения
        parent - родительская папка, если None, то создается главное меню
        welcome - надпись в рамке 40
        command_list - список объектов вложенных папок
    '''
    def __init__(self, name, parent, welcome='Добро пожаловать в адресную книгу ntone!'):
        self.name = name
        self.parent = parent
        if parent:
            self.parent.show_list.append(self.name)
            self.parent.command_list.append(self)
        self.show_list = []
        self.command_list = [] 
        self.terminal_window = shutil.get_terminal_size((80,20))     
        self.welcome = (int(self.terminal_window.columns / 2 - 20) * '=' + '{namemenu}' + int(self.terminal_window.columns / 2 - 20) * '='+'\n' * (self.terminal_window.lines-len(self.command_list)-7)).format(namemenu = welcome)

    def show_menu(self):
        """Отображение меню"""
        print(self.welcome)      
        for i in range(1,len(self.show_list)+1):
            print('{n}. {command}'.format(n = i, command = self.show_list[i - 1]))

    def choose_command(self):
        '''Отображение меню и выбор команды '''
        while True:
            self.show_menu()
            current_command = int(input('Выберите комманду: ')) - 1
            if current_command >= len(self.command_list):
                print('неверная команда')
                continue
            if current_command == len(self.command_list) - 1: break
            if isinstance(self.command_list[current_command], Command):
                self.command_list[current_command].run_command()
            if isinstance(self.command_list[current_command], Menu):
                self.command_list[current_command].show_menu()
                self.command_list[current_command].choose_command()


class Command(object):
    """Класс используемых комманд в меню"""
    def __init__(self, name, parent, function = None):
        self.name = name
        self.parent = parent
        self.parent.show_list.append(self.name)
        self.parent.command_list.append(self)
        self.function = function

    def run_command(self):
        """Запуск команды"""
        print('run_command')
        self.function()

        
        


