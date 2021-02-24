import sys
from file_manager_1 import create_file, create_folder, get_list, delete_file, copy_file, safe_info, change_dir

safe_info('Start')

try:
    command = sys.argv[1]
except IndexError:
    print('You forgot to select the command')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Write the file name and try again!')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Write the folder name and try again!')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Write the file or folder name and try again!')
        else:
            delete_file(name)
    elif command == 'change_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Write the file or folder name and try again!')
        else:
            change_dir(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Check the file or folder name and new name and try again!')
        else:        
            copy_file(name, new_name)
    elif command == 'help':
        print('list - list of files and flders')
        print('create_file - create a file')
        print('create_folder - create a folder')
        print('delete - delete a file or folder')
        print('copy - copy a file or folder')

    safe_info('The end')