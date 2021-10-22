import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir

save_info('Start')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду. help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести название папки')
        else:
            delete_file(name)
    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя папки')
        else:
            change_dir(name)
    elif command == 'cope':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Необходимо ввести название файла и название копии')
        else:
            copy_file(name, new_name)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файлв или папки')

save_info('End')
