from importlib import import_module
from time import sleep
import sys
import logging

def print_error(message):
    print(message)
    for sec in range(0, 13):
        msg = '#' + '=' * sec + '>'
        print(msg, end='\r')
        sleep(0.05)
    print('==============>$')

def user_input(message, choice):
    while True:
        choice = input(str(message))
        options = ['y', 'n']

        for option in options:
            if choice != option:
                pass
            else:
                return choice

        print_error('* Enter y or n *')
        continue

def main():
    module = input(str('Choose a module to import:\n'))
    mod = import_module(module)

    if module == '':
        print_error('* No package was selected. *\n')
    else:
        contents = dir(mod)

    list(contents)
    [ print(content) for content in contents ]

    choice = ''
    user_input('Want to save the list to a file?\n', choice)

    if choice == 'n':
        sys.exit(0)

    with open('C:\\Users\\Public\\ModuleOut.txt', 'a') as file:
        [ file.write(content + '\n') for content in contents ]

    print('All finished!!!')

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('* Ctrl + C detected ... exiting *')

    except Exception as ex:
        logging.exception('* Error Ocurred: {} *'.format(ex))