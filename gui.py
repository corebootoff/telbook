import shutil
import sys
import models

main = models.Menu('Главное меню', None)

tel_menu = models.Menu('Телефонная книга', main)
show_all = models.Command('Посмотреть всю книгу', tel_menu)
add_contact = models.Command('Добавить контакт', tel_menu)
remove_contact = models.Command('Удалить контакт', tel_menu)
exit_tel_menu = models.Command('Назад', tel_menu)

site_menu = models.Menu('Книга сайтов', main)
preferences = models.Menu('Настройки', main)
exit_main = models.Command('Выход', main)

main.choose_command()