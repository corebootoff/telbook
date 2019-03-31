import shutil
import sys


class Menu(object):
    """
       welcome      название заголовка. фиксированная длина 40 символов
       parent       имя модуля родителя
       show_list    меню для отображения
       command_list содержит словарь с номером и соответствующей функцией
    """
    terminal_window = shutil.get_terminal_size((80,20)) 
    SEPARATOR = '=' * terminal_window.columns
    WELCOME = '\n' * terminal_window.lines + int(terminal_window.columns / 2 - 20) * '=' + {namemenu} + int(terminal_window.columns / 2 - 20) * '='
    def __init__(self, parent, show_list, command_list, welcome=NAMEMENU['main']):
        self.parent = parent
        self.show_list = show_list
        self.welcome = welcome
        self.command_list = command_list

    def show_menu(self):
        
        print(self.SEPARATOR)
        print(self.WELCOME.format(namemenu = self.welcome))
        for i in range(1,len(self.command_list)+1):
            print('{n}. {command}'.format(n = i, command = self.command_list[i - 1]))

    def choose_command(self):
        while True:
            current_command = input('Выберите комманду: ')
            try:
                command_list[current_command]
            except KeyError: 
                print('неверная команда')
                continue





